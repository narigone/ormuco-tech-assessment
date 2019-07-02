from threading import Thread


class ThreadWithReturnValue(Thread):
    def run(self):
        if self._target is None:
            return
        self._return = None
        self._return = self._target(*self._args, **self._kwargs)

    def join(self, timeout=None):
        super().join(timeout)
        return self._return
