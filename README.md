
## git-keeper report data

This script generates CSV files containing data about git-keeper submissions. It is designed to be used in a folder created by `gkeep fetch` that contains all the assignments for a single course.  It will create a file with the following columns:

* `student_id` (hex string) - an MD5 hash of the username folder for each student
* `course_name` (string) - the name of the course
* `assignment_number` (int) - ordinal numbers for each assignment
* `assignment_name` (string) - the `git-keeper` name for each assignment
* `num_submissions` (int) - the number of times the student submitted
* `success` (boolean) - whether the student achieved success in the final submission

## Setup

* Create a virtual environment
* `pip install .` in the folder.  This will create a script named `report`

## Execution

* Goto a folder that contains one or more folders created by `gkeep fetch`
* Create a file such as `assignments.txt` that contains the assignments in the order they were due in the course
* Run `report <course_id> assignments.txt <success_string> <output_path>`

