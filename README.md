1. Pull this repository into your local machine by following these steps:
    - copy the url from this repository
    -  git clone 'repo' in the cmd
2. change branches to insecure - git checkout insecure
3. check the commented code in task_list.html and uncomment it to allow vulnerabilities into the application (XSS attack)
    task_list.html: 
       <!-- xss attack script -->
      <!-- <p id="maliciousScript"></p>
      <script>
          // Stored XSS
          var maliciousScript = document.createElement('script');
          maliciousScript.textContent = "alert('Stored XSS Attack!');";
          document.getElementById('maliciousScript').appendChild(maliciousScript);
      </script>   -->
4. Create two user accounts with different tasks. Login into one user and search for a task the other user has by their task id for example "/tasks/10". (Sensitive data exposed)
5. Switch to the secure branch - git checkout secure
6. This branch contains added code that secures the vulnerabilities above:
   - middleware.py for security headers
   - Securing sensitve data in views.py
     
       # This method secures the sensitive data
    def get(self, request, *args, **kwargs):
        task = self.get_object()

        # If the logged-in user is the owner of the task, the task details will become available
        if task.user == request.user:
            return super().get(request, *args, **kwargs)
        else:
            logger.warning("Unauthorized access attempt to task details")
            return redirect('unauthorized_access')
   
   - logging and monitoring in settings.py which created a django.log file inside the toDoListProject folder

