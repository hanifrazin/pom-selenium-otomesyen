class LoginData:
    username = 'standard_user'
    password = 'secret_sauce'
    other_users_list = [
        ('problem_user',),
        ('performance_glitch_user',),
        ('error_user',),
        ('visual_user',)
    ]
    blocked_user = 'locked_out_user'
    blocked_error_msg = "Epic sadface: Sorry, this user has been locked out."
    el_neg_display = 'Element is not displayed'
    empty_usr_msg = 'Epic sadface: Username is required'
    empty_pass_msg = 'Epic sadface: Password is required'
    invalid_cred_msg = 'Epic sadface: Username and password do not match any user in this service'
    creds_neg_list = [
        ('standard_users', password, invalid_cred_msg),
        ('problem_users', password, invalid_cred_msg),
        ('performances_glitch_users', password, invalid_cred_msg),
        ('errors_users', password, invalid_cred_msg),
        ('visuals_users', password, invalid_cred_msg),
        ('problem_users', password, invalid_cred_msg),
        ('standard_user', password+'s', invalid_cred_msg),
        ('problem_user', password+'s', invalid_cred_msg),
        ('performances_glitch_user', password+'s',invalid_cred_msg),
        ('errors_user', password+'s', invalid_cred_msg),
        ('visuals_user', password+'s', invalid_cred_msg),
        ('problem_user', password+'s', invalid_cred_msg),
        ('', '', empty_usr_msg),
        ('', password, empty_usr_msg),
        ('standard_user', '', empty_pass_msg),
        ('problem_user', '', empty_pass_msg),
        ('performances_glitch_user', '', empty_pass_msg),
        ('errors_user', '', empty_pass_msg),
        ('visuals_user', '', empty_pass_msg),
        ('problem_user', '', empty_pass_msg),
        ('standard_users', '', empty_pass_msg),
        ('problem_users', '', empty_pass_msg),
        ('performances_glitch_users', '', empty_pass_msg),
        ('errors_users', '', empty_pass_msg),
        ('visuals_users', '', empty_pass_msg),
        ('problem_users', '', empty_pass_msg),
    ]
