# Sing Up
post => http://127.0.0.1:8000/api/account/sing-up/
=) passing data fields: email, profile_picture, username, password, first_name, last_name

# Account Verification
post => http://127.0.0.1:8000/api/account/verify/
=) passing data fields: otp
    {
        "otp":"265235"
    }

# Login
post => http://127.0.0.1:8000/api/account/login/
=) passing data fields: username, password
    {
        "username":"mossaddak",
        "password":"1234"
    }

# User Own Profile
get, patch => http://127.0.0.1:8000/api/account/profile/
=) passing data fields: username, password, first_name, last_name, email, profile_picture
note: Must need "username" field

# Get user information as an Admin
get => http://127.0.0.1:8000/api/account/profile/
post, patch, delete => http://127.0.0.1:8000/api/account/profile/<user_id>/
Note:only super admin has this permission
