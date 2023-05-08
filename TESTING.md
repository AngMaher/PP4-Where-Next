## Testing

Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

As my project uses Jinja syntax, such as `{% for loops %}`, `{% url 'home' %}`, and `{{ variable|filter }}`
it will not validate properly if I copy and paste into the HTML validator straight from my source files.

Usually in order to properly validate these types of files, it's recommended to
[validate by uri](https://validator.w3.org/#validate_by_uri) from the deployed Heroku pages.

Unfortunately, nearly all of the pages on this site require a user to be logged-in and authenticated,
and will not work using this method, due to the fact that the HTML Validator (W3C) doesn't have
access to login to the pages.

In order to properly validate my HTML pages with Jinja syntax for authenticated pages, I followed these steps:

- Navigate to the deployed pages which require authentication
- Right-click anywhere on the page, and select **View Page Source** (usually `CTRL+U` or `⌘+U` on Mac).
- This will display the entire "compiled" code, without any Jinja syntax.
- Copy everything, and use the [validate by input](https://validator.w3.org/#validate_by_input) method.
- Repeat this process for every page that requires a user to be logged-in/authenticated.

| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftribe.herokuapp.com%2F) | ![screenshot](documentation/testing/html-validation-home.png) | Pass: No Errors |
| Sign Up | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftribe.herokuapp.com%2Faccounts%2Fsignup%2F) | ![screenshot](documentation/testing/html-validation-sign-up.png) | Pass: No Errors |
| Log In | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftribe.herokuapp.com%2Faccounts%2Flogin%2F) | ![screenshot](documentation/testing/html-validation-sign-in.png) | Pass: No Errors |
| About | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftribe.herokuapp.com%2Faccounts%2Fpassword%2Freset%2F) | ![screenshot](documentation/testing/html-validation-forgot-password.png) | Pass: No Errors |
| Blog | n/a | ![screenshot](documentation/testing/html-validation-feed.png) | Pass: No Errors |
| All Posts Feed | n/a | ![screenshot](documentation/testing/html-validation-all-posts-feed.png) | Pass: No Errors |
| Blog Content | n/a | ![screenshot](documentation/testing/html-validation-inbox.png) | Pass: No Errors |
| Messaging Thread | n/a | ![screenshot](documentation/testing/html-validation-message-thread.png) | Pass: No Errors |
| Bucket List | n/a | ![screenshot](documentation/testing/html-validation-create-thread.png) | Pass: No Errors |
| Add Item | n/a | ![screenshot](documentation/testing/html-validation-user-profile.png) | Pass: No Errors |
| Edit Item| n/a | ![screenshot](documentation/testing/html-validation-other-profile.png) | Pass: No Errors |
| Add Plan | n/a | ![screenshot](documentation/testing/html-validation-edit-profile.png) | Pass: No Errors |
| Edit Plan | n/a | ![screenshot](documentation/testing/html-validation-followers-list.png) | Pass: No Errors |
| Individual Post | n/a | ![screenshot](documentation/testing/html-validation-individual-post.png) | Pass: No Errors |
| Delete Bucket List item | n/a | ![screenshot](documentation/testing/html-validation-delete-post.png) | Pass: No Errors ||
| Sign Out | n/a | ![screenshot](documentation/testing/html-validation-sign-out.png) | Pass: No Errors |

### PEP8

- [PEP8CI](https://pep8ci.herokuapp.com/) - This was used test the code. No errors where found in the code. 

| File | folder/app | Screenshot | Notes |
| --- | --- | --- | --- |
| admin.py | Bucketlist | ![screenshot](/media/readme/pep8/pep8-bucketlist-admin.png) | No errors found |
| apps.py | Bucketlist | ![screenshot](/media/readme/pep8/pep8-bucketlist-apps.png) | No errors found |
| forms.py | Bucketlist | ![screenshot](/media/readme/pep8/pep8-bucketlist-forms.png) | No errors found |
| models.py | Bucketlist | ![screenshot](/media/readme/pep8/pep8-bucketlist-models.png) | No errors found |

| admin.py | Bucketlist | ![screenshot](/media/readme/pep8/pep8-bucketlist-admin.png) | No errors found |
| apps.py | Bucketlist | ![screenshot](/media/readme/pep8/pep8-bucketlist-apps.png) | No errors found |
| forms.py | Bucketlist | ![screenshot](/media/readme/pep8/pep8-bucketlist-forms.png) | No errors found |
| models.py | Bucketlist | ![screenshot](/media/readme/pep8/pep8-bucketlist-models.png) | No errors found |



### Manual Testing

Please find manual testing file here: [TESTING.md](/TESTING.md)

### Bugs/known issues