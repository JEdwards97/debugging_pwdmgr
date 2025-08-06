# == INSTRUCTIONS ==
#
# Purpose: Manage a user's (valid) passwords
#
# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: add
#      Purpose: add a password for a service IF it is valid, otherwise do nothing
#      Arguments: one string representing a service name,
#                 one string representing a password
#      Returns: None
#   3. Name: remove
#      Purpose: remove a password for a service
#      Arguments: one string representing a service name
#      Returns: None
#   4. Name: update
#      Purpose: update a password for a service IF it is valid, otherwise do nothing
#      Arguments: one string representing a service name,
#                 one string representing a password
#      Returns: None
#   5. Name: list_services
#      Arguments: none
#      Returns: a list of all the services for which the user has a password
#   6. Name: sort_services_by
#      Arguments: A string, either 'service' or 'added_on',
#                 (Optional) A string 'reverse' to reverse the order
#      Returns: a list of all the services for which the user has a password
#               in the order specified
#   7. Name: get_for_service
#      Arguments: one string representing a service name
#      Returns: the password for the given service, or None if none exists
#
# A reminder of the validity rules:
#   1. A password must be at least 8 characters long
#   2. A password must contain at least one of the following special characters:
#      `!`, `@`, `$`, `%` or `&`
#
# And a new rule: passwords must be unique (not reused in other services).
#
# Example usage:
#   > password_manager = PasswordManager2()
#   > password_manager.add('gmail', '12ab5!678')   # Valid password
#   > password_manager.add('facebook', '$abc1234') # Valid password
#   > password_manager.add('youtube', '3@245256')  # Valid password
#   > password_manager.add('twitter', '12345678')  # Invalid password, so ignored
#   > password_manager.get_for_service('facebook')
#   '$abc1234'
#   > password_manager.list_services()
#   ['gmail', 'facebook', 'youtube']
#   > password_manager.remove('facebook')
#   > password_manager.list_services()
#   ['gmail', 'youtube']
#   > password_manager.update('gmail', '12345678')  # Invalid password, so ignored
#   > password_manager.get_for_service('gmail')
#   '12ab5!678'
#   > password_manager.update('gmail', '%21321415')  # Valid password
#   > password_manager.get_for_service('gmail')
#   '%21321415'
#   > password_manager.sort_services_by('service')
#   ['gmail', 'youtube']
#   > password_manager.sort_services_by('added_on', 'reverse')
#   ['youtube', 'gmail']

# There are many more examples possible but the above should give you a good
# idea.

# == YOUR CODE ==
from datetime import datetime
class PasswordManager2():
    def __init__(self): #Done 
        self.password_mgr = {} 

    def add(self, service_name, password):#Done 
        if len(password) > 7 and any(char in password for char in '!@$%&'):
            if password in [p['password'] for p in self.password_mgr.values()]:
                return 
            self.password_mgr[service_name] = { 
                'password': str(password),
                'added_on': datetime.now()
            }
            
    def remove(self, service_name): #Done
        if service_name in self.password_mgr: 
            del self.password_mgr[service_name]

    def update(self, service_name, password): #Done 
        if len(password) > 7 and any(char in password for char in '!@$%&'):
            if password in [p['password'] for p in self.password_mgr.values()]:
                return 
            self.password_mgr[service_name] = { 
                'password': str(password),
                'added_on': datetime.now()
            }

    def list_services(self): #Done
        return list(self.password_mgr.keys())
    
    def sort_services_by(self, sort_by, reverse=False): #Done 
        if sort_by == 'service':
            return sorted(self.password_mgr.keys(), reverse=reverse)
        elif sort_by == 'added_on':
            sorted_items = sorted(self.password_mgr.items(), key=lambda item:item[1]['added_on'], reverse=reverse)
            return [s for s, info in sorted_items]
            
        
    def get_for_service(self, service_name): #Done 
        record = self.password_mgr.get(service_name)
        if record: 
            return record['password']
        return None
    