# Advanced Features and Security

## Custom User Model

- Implemented using AbstractUser
- Added date_of_birth and profile_photo fields
- Configured via AUTH_USER_MODEL

## Permissions and Groups

- Custom permissions: can_view, can_create, can_edit, can_delete
- Groups:
  - Viewers: can_view
  - Editors: can_view, can_create, can_edit
  - Admins: all permissions
- Permissions enforced using @permission_required decorators

## Security Best Practices

- CSRF protection enabled in templates
- ORM used to prevent SQL injection
- CSP middleware configured
- Secure cookies enforced

## HTTPS and Secure Redirects

- HTTPS enforced via SECURE_SSL_REDIRECT
- HSTS configured
- Secure headers enabled
