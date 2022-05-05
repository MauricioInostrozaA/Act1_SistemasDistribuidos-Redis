# SD_Tarea1
Integrantes: Luis Donoso, Mauricio Inostroza

## Configuración Redis
Actualmente se tiene una configuración de 2mb, de memoria máxima y con una política de remoción LFU (Least Frecuently Used) 

Si se desea cambiar esto, dentro del archivo **overrides.conf**

Por ejemplo:

```python
maxmemory 10mb
maxmemory-policy allkeys-lru
```
