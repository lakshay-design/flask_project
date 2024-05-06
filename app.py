import boto3
from flask import Flask, jsonify

app = Flask(__name__)

def list_s3_buckets():
    try:
        # Create a boto3 S3 client
        s3_client = boto3.client('s3')

        # Get the list of S3 buckets
        buckets = s3_client.list_buckets()['Buckets']

        # Return the list of bucket names
        return [bucket['Name'] for bucket in buckets]
    except Exception as e:
        # Handle exceptions
        return {"error": str(e)}

@app.route('/s3/buckets', methods=['GET'])
def get_s3_buckets():
    bucket_list = list_s3_buckets()
    if 'error' in bucket_list:
        return jsonify(bucket_list), 500
    return jsonify(bucket_list), 200

if __name__ == '__main__':
    app.run(debug=True)
