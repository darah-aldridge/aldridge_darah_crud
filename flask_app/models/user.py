from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_cr').query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users
    @classmethod
    def get_one(cls, id):
        query  = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL('users_cr').query_db(query, {'id':id})
        print(result)
        return cls(result[0])
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users ( first_name , last_name , email) VALUES ( %(fname)s , %(lname)s , %(email)s);"
        return connectToMySQL('users_cr').query_db( query, data )  
    @classmethod
    def update(cls, data, id):
        query = f"UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s WHERE id = {id};"
        return connectToMySQL('users_cr').query_db(query,data)
    @classmethod
    def delete(cls, id):
        query  = f"DELETE FROM users WHERE id = {id};"
        return connectToMySQL('users_cr').query_db(query)

    
