# app.py
from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

# HTTP Status Codes Database
HTTP_CODES = {
    "100": {
        "title": "Continue",
        "type": "Informational",
        "description": "The server has received the request headers and the client should proceed to send the request body.",
        "solutions": ["Verify if the request body is being sent correctly", "Check if the Expect header is being used properly"],
        "severity": "low"
    },
    "200": {
        "title": "OK",
        "type": "Success",
        "description": "The request was successful.",
        "solutions": ["Standard successful response, no action needed"],
        "severity": "none"
    },
    "301": {
        "title": "Moved Permanently",
        "type": "Redirection",
        "description": "The requested resource has been permanently moved to a new URL.",
        "solutions": [
            "Update your bookmarks and links",
            "Implement proper redirect handling in your client",
            "Update any hardcoded URLs in your code"
        ],
        "severity": "medium"
    },
    "400": {
        "title": "Bad Request",
        "type": "Client Error",
        "description": "The server cannot process the request due to a client error.",
        "solutions": [
            "Verify the request syntax",
            "Check request parameters and headers",
            "Validate input data format"
        ],
        "severity": "high"
    },
    "404": {
        "title": "Not Found",
        "type": "Client Error",
        "description": "The requested resource could not be found on the server.",
        "solutions": [
            "Verify the URL is correct",
            "Check if the resource exists",
            "Review your routing configuration"
        ],
        "severity": "high"
    },
    "429": {
        "title": "Too Many Requests",
        "type": "Client Error",
        "description": "The user has sent too many requests in a given amount of time.",
        "solutions": [
            "Implement rate limiting in your client",
            "Add request throttling",
            "Cache responses when possible",
            "Review API usage patterns"
        ],
        "severity": "high"
    },
    "500": {
        "title": "Internal Server Error",
        "type": "Server Error",
        "description": "The server encountered an unexpected condition that prevented it from fulfilling the request.",
        "solutions": [
            "Check server logs for errors",
            "Debug server-side code",
            "Verify server configuration",
            "Implement proper error handling"
        ],
        "severity": "critical"
    },
    "502": {
        "title": "Bad Gateway",
        "type": "Server Error",
        "description": "The server received an invalid response from the upstream server.",
        "solutions": [
            "Check upstream server status",
            "Verify network connectivity",
            "Review proxy configuration",
            "Check server logs"
        ],
        "severity": "critical"
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/status/<code>')
def get_status(code):
    if code in HTTP_CODES:
        return jsonify(HTTP_CODES[code])
    return jsonify({
        "error": "Code not found",
        "message": "The specified HTTP status code is not in our database."
    }), 404

if __name__ == '__main__':
    app.run(debug=True)