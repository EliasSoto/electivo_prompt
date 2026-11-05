# Tarea Práctica: SPDD y Control del Estado 🚀

**Unidad III:** Metodologías Habilitadas por IA
**Clase 8:** Structured PDD (SPDD)

## 🎯 Objetivo de la Tarea
Aplicar la metodología SPDD (Structured Prompt-Driven Development) desde cero. Deberás construir un Canvas de Razonamiento formal (archivo `.prompt`) para generar un módulo de cálculo de envíos que pase una batería de pruebas estricta. 

## 🚫 Regla de Oro (Tolerancia Cero)
**Está estrictamente prohibido escribir o editar manualmente el archivo de código fuente generado (`shipping_calculator.py`).** Toda la lógica, corrección de errores (bugs) y arquitectura debe resolverse modificando tu archivo `.prompt` y regenerando el código con la IA.

---

## 🏢 Contexto de Negocio
El equipo de Logística requiere un nuevo módulo para calcular los costos de envío. Han definido las siguientes reglas de negocio:

1. El costo base de envío estándar nacional ('NATIONAL') es de **$10.0**.
2. Si el total del carrito del cliente es **igual o mayor a $100.0**, el envío base nacional pasa a ser **Gratis ($0.0)**.
3. Si el cliente selecciona envío Express (`is_express=True`), se debe sumar un recargo fijo de **$15.0** al costo de envío (incluso si el envío base era gratis).
4. Si el destino es Internacional ('INTERNATIONAL'), el costo final del envío (base + express) **se multiplica por 2.0**.
5. Cualquier otro destino desconocido debe levantar un error `ValueError`.

## 🛠️ Instrucciones Paso a Paso

### Paso 1: Preparación del Entorno
1. Crea una nueva carpeta para esta tarea.
2. Descarga el archivo de pruebas `test_shipping.py` que te ha proporcionado el profesor y guárdalo en la carpeta.

### Paso 2: Diseño de Intenciones (El Artefacto)
1. Crea un archivo llamado `shipping_calculator.prompt` en tu carpeta.
2. Basándote en la plantilla del "Canvas de Razonamiento" vista en clase, redacta tu prompt estructurado. Asegúrate de incluir:
   - **Intención Core:** ¿Qué hace la clase y cuál es la firma del método principal? (Ej. `calculate_shipping(cart_total: float, is_express: bool, destination: str) -> float`).
   - **Reglas de Negocio:** Traduce el contexto de negocio de arriba a reglas claras para el LLM.
   - **Anti-Metas:** Restricciones explícitas (Ej. Cero dependencias externas, no crear bases de datos).

### Paso 3: Generación Pura
1. Alimenta tu archivo `shipping_calculator.prompt` a tu agente IDE (Cursor, Copilot, LM Studio) o pégalo en un LLM (ChatGPT/Claude).
2. Pídele que genere el archivo `shipping_calculator.py`. 
3. Guarda el archivo generado en tu carpeta. **¡No lo edites manualmente!**

### Paso 4: Auditoría (Trazabilidad)
1. Ejecuta las pruebas en tu terminal:
   ```bash
   python -m unittest test_shipping.py
   ```
2. **Si las pruebas fallan:**
   - Lee el error en la consola.
   - Abre tu archivo `shipping_calculator.prompt` y mejora la redacción de tus reglas de negocio o especificaciones técnicas.
   - Pide a la IA que regenere `shipping_calculator.py` reemplazando el anterior.
   - Vuelve a correr las pruebas. Repite hasta obtener **OK**.

---

## 📦 Entregables
Deberás subir a la plataforma (o repositorio Git) un archivo `.zip` que contenga los siguientes **3 archivos**:
1. `shipping_calculator.prompt` (Tu Canvas de Razonamiento final).
2. `shipping_calculator.py` (El código generado por la IA, sin alteraciones humanas).
3. `test_shipping.py` (El script de pruebas original).

*Criterio de Evaluación: Se revisará la claridad, estructura y restricciones de tu archivo `.prompt`, y se verificará que el código Python generado por dicho prompt pase los tests exitosamente.*
