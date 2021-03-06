import sqlite3
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
import datetime
from hrapp.models import TrainingProgram
from ..connection import Connection


def training_program_past(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                t.id,
                t.training_title,
                t.start_date,
                t.end_date,
                t.max_capacity
            from hrapp_trainingprogram t
            where t.start_date < CURRENT_DATE
            """)

            all_training_programs = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                training_program = TrainingProgram()
                training_program.id = row['id']
                training_program.training_title = row['training_title']
                training_program.start_date = row['start_date']
                training_program.end_date = row['end_date']
                training_program.max_capacity = row['max_capacity']

                all_training_programs.append(training_program)

        template = 'training_programs/training_program_past.html'
        context = {
            'training_programs': all_training_programs
        }

        return render(request, template, context)
