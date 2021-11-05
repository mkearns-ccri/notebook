import os


class FileLogger:

    def __init__(self, audit_dir='/opt/jupyterhub/logs', audit_file="audit.log"):

        # create audit directory if it doesn't exist yet
        if not os.path.exists(audit_dir):
            os.makedirs(audit_dir)

        self._audit_path = os.path.join(audit_dir, audit_file)

    def log(self, msg):
        """
        Append the message to the audit log.
        """
        with open(self._audit_path, 'a') as out_file:
            out_file.write(self._format(msg))

    def _format(self, msg):
        """
        Format the message for logging.
        """
        return str(msg) + '\n'