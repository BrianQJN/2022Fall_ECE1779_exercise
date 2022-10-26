# Update the path below.
file = '~/.aws/credentials'

# Update keys below.
AWS_ACCESS_KEY_ID = 'AKIA56I62COEQW5DLOU7'
AWS_SECRET_KEY = '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'


with open(file, 'w') as filetowrite:
    myCredential = f"""[default]
aws_access_key_id={AWS_ACCESS_KEY_ID}
aws_secret_access_key={AWS_SECRET_KEY}
"""
    filetowrite.write(myCredential)

# Update the path below.
file = '~/.aws/config'

with open(file, 'w') as filetowrite:
    myCredential = """[default]
                      region = us-east-1
                      output = json
                      [profile prod]
                      region = us-east-1
                      output = json"""
    filetowrite.write(myCredential)
