# therame
Mental Health check ins using Alexa and Fitbit built for Bitcamp 2017

# Running
1. Clone the github repository locally
2. Install Python and all modules in `~$ pip install -r requirements.txt`
3. Test the app by running locally `~$ python ./web-server/application.py`
4. Set your aws credentials, most likely located in `~/.aws/credentials`
5. Use `eb` to create a new elastic beanstalk instance or update `./web-server/.elasticbeanstalk/config.yml` to point to an existing instance.
6. Deploy to aws `~$ eb deploy`

# Example Elastic Beanstalk config.yml
```
branch-defaults:
  default:
    environment: my-server-dev
    group_suffix: null
global:
  application_name: my-server
  branch: null
  default_ec2_keyname: my_keyname
  default_platform: Python 2.7
  default_region: us-east-1
  profile: eb-cli
  repository: null
  sc: null
```

# Troubleshooting Tips
[Installing the awscli in order to use eb.](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install.html)

`environment` should match the name of an elastic beanstalk server in your aws management console.

If you create a new elastic beanstalk instance using eb and don't see it show up in your management console you should check that you correctly set you public and secret keys in `~/.aws/credentials`.

Also check for environment variables that may be overriding your default credentials `~$ echo $AWS_ACCESS_KEY_ID && echo $AWS_SECRET_ACCESS_KEY`.
