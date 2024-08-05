# ve3task

for ve3 internship technical assessment

simply clone the repo and run 'python3 manage.py runserver' at the root directory.

The 'task' app sits at 127.0.0.1:8000

Select the file you want to upload and click 'upload'. You will see the results in a few moments.

No Models were used. Only views.py and urls.py were used along with forms.py. The form set up in upload.html in templates folder makes a POST request when 'upload' is clicked and the data.csv file is saved to disk by the logic in views.py. Then the same file is read and processed by the a piece of python code using pandas. The print out put and histogram are saved to disk. This is then used by the template file 'upload.html' to display the results on the same page.
