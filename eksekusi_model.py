#eksekusi_model.py

import tensorflow as tf

def eksekusi_model(model, data, perangkat='CPU'):
    if perangkat == 'GPU':
        with tf.device('/GPU:0'):
            hasil = model.predict(data)
    elif perangkat == 'TPU':
        # Implementasi eksekusi TPU
        pass
    else:
        hasil = model.predict(data)
    return hasil
