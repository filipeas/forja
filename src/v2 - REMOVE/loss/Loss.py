class Loss(object):
    def loss(self, y_true, y_pred):
        return NotImplementedError()
    
    def gradient(self, y_true, y_pred):
        raise NotImplementedError()
    
    def acc(self, y_true, y_pred):
        return 0