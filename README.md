[![CircleCI](https://circleci.com/gh/GovWizely/lambda-bitly.svg?style=svg)](https://circleci.com/gh/GovWizely/lambda-bitly)
[![Maintainability](https://api.codeclimate.com/v1/badges/3bae281b0bf0a812206e/maintainability)](https://codeclimate.com/github/GovWizely/lambda-bitly/maintainability)

# Lambda Bitly

This project provides a simple AWS Lambda around [Bitly's URL Shortener service](https://dev.bitly.com/get_started.html).
It has a retry mechanism to 
work around Bitly's rate limiting. The idea is to call this Lambda, probably via an AWS API Gateway, 
instead of Bitly's API when you want a
shortened URL and would rather wait a bit for an answer than get an error message about exceeding rate limits.

## Prerequisites

- This project is tested against Python 3.7+ in [CircleCI](https://app.circleci.com/github/GovWizely/lambda-bitly/pipelines).
- Make sure you have your [Bitly API generic access token](https://dev.bitly.com/get_started.html) handy.

### Local Development

```bash
git clone git@github.com:GovWizely/lambda-bitly.git
cd lambda-bitly
mkvirtualenv -p /usr/local/bin/python3.8 -r requirements-test.txt lambda-bitly
```

If you are using PyCharm, make sure you enable code compatibility inspections for Python 3.7/3.8.

### Tests

```bash
python -m pytest
```

## Configuration

* Define the Bitly API generic access token as an environment variable `export BITLY_GENERIC_ACCESS_TOKEN=your_token`.
* Define AWS credentials in either `config.yaml` or in the [default] section of `~/.aws/credentials`. To use another profile, you can do something like `export AWS_DEFAULT_PROFILE=govwizely`.
* Edit `config.yaml` if you want to specify a different AWS region, role, and so on.
* Make sure you do not commit the AWS credentials to version control.

## Invocation

	lambda invoke -v
 
## Deploy
    
In the AWS Lambda console, set up the `BITLY_GENERIC_ACCESS_TOKEN` environment variable. Then you are ready to deploy:

	lambda deploy --requirements requirements.txt
