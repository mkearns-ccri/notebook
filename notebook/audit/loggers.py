import os

class FileLogger:

    def __init__(self, audit_dir='/opt/jupyterhub/logs', audit_file="audit.log", msg_type='execute_request'):

        # create audit directory is it doesn't exist yet
        if not os.path.exists(audit_dir):
            os.makedirs(audit_dir)

        self._audit_path = os.path.join(audit_dir, audit_file)
        self._msg_type = msg_type

    def log(self, msg_type, msg):
        """
        Append the message to the audit log.
        """
        if msg_type == self._msg_type:
            with open(self._audit_path, 'a') as out_file:
                out_file.write(self._format(msg))

    def _format(self, msg):
        """
        Format the message for logging.
        """
        return msg