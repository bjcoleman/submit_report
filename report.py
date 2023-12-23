import os
import sys
import hashlib
import click


def determine_success(reports, base_dir, success_string):
    if len(reports) == 0:
        return False
    
    last_report = reports[-1]
    with open(os.path.join(base_dir, last_report), 'r') as f:
        if success_string in f.read():
            return True
    return False    


@click.command()
@click.argument('course_name')
@click.argument('assignment_list_path', type=click.File('r'))
@click.argument('success_string')
@click.argument('output_path', type=click.Path())
def generate_report(course_name, assignment_list_path, success_string, output_path):

    with open(output_path, 'w') as f:

        assignment_number = 0
        for assignment_name in assignment_list_path:
            assignment_number += 1
            assignment_name = assignment_name.strip()

            if assignment_name == '':
                continue

            base_dir = os.path.join(assignment_name, 'reports')

            for directory in sorted(os.listdir(base_dir)):
                if not os.path.isdir(base_dir + '/' + directory) or directory == '.git':
                    continue

                m = hashlib.md5()
                m.update(directory.encode('utf-8'))
                hash = m.hexdigest()
                
                base_path = base_dir + '/' + directory
                reports = [name for name in sorted(os.listdir(base_path)) if name.startswith('report')]

                successful = determine_success(reports, base_path, success_string)

                print(','.join([hash, course_name, str(assignment_number), assignment_name, str(len(reports)), str(successful)   ]), file=f)