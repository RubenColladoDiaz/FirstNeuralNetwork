import tensorflow as tf # Liberia de IA hecha por Google
import numpy as np # Libreria para trabajar con arreglos numéricos
import matplotlib.pyplot as plt

# Ejemplos que la red usará para aprender
celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

# Capa densa: Capa con conexiones desde cada neurona hacia todas las
# neuronas de la siguiente capa.
# En nuestro ejemplo de transformar de celsius a fahrenheit solo tendremos
# dos neuronas.
capa = tf.keras.layers.Dense(units=1, input_shape=[1]) # 1 neurona, 1 entrada (Celsius)
modelo = tf.keras.Sequential([capa]) # Las capas se apilarán una tras otra, en orden

modelo.compile(
    optimizer = tf.keras.optimizers.Adam(0.1), # Tasa de aprendizaje 0.1
    loss='mean_squared_error' # Aproximar a valores reales
)

print("Comenzando entrenamiento...")
historial = modelo.fit(celsius, fahrenheit, epochs=1000, verbose = False) # epochs = Num de vueltas por los datos
print("Modelo entrenado!")

plt.xlabel("# Epoca")
plt.ylabel("Magnitud de pérdida")
plt.plot(historial.history["loss"])
plt.show()

print("Hagamos una predicción!")
resultado = modelo.predict(np.array([[100.0]]))
print("El resultado es " + str(resultado) + " fahrenheit!")

print("Variables internas del modelo")
print(capa.get_weights())