class ResponseCommon:
    """
    Common response structure for API responses.
    """
    def __init__(self, code: int, success: bool, message: str, data):
        self.code = code
        self.success = success
        self.message = message
        self.data = data
        

    def to_json(self):
        """
        Returns a success response.
        :param data: The data to return in the response.
        :param message: A success message.
        :return: A dictionary representing the success response.
        """
        return {
            "code": self.code,
            "success": self.success,
            "message": self.message,
            "response":self.data
        }

    def to_json_data(self):
        """
        Returns an error response.
        :param message: An error message.
        :param status_code: The HTTP status code for the error.
        :return: A dictionary representing the error response.
        """
        return {
            "message": self.message,
            "response":self.data,
        }
