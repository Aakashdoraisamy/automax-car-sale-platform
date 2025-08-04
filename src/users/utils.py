def user_directory_path(instance, filename):
    return 'users/{0}/{1}'.format(instance.user.id, filename)