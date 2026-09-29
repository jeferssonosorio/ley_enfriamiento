# Ley de Enfriamiento de Newton

Aplicación web desarrollada para la asignatura de Matemáticas (Quiz 1) que implementa el modelo para la **Ley de Enfriamiento de Newton**. 
El proyecto está organizado en un monorepo con **backend** (API REST en Django) y **frontend** (SPA en Vue 3).

---

## 🏗️ Estructura y Arquitectura del Proyecto

### Backend (Django + DRF)
Proporciona el motor de cálculo exacto.
- Implementado en `backend/local_apps/ley_enfriamiento`.
- No requiere base de datos ni autenticación.
- Calcula la constante de proporcionalidad térmica **$k$** en base a 4 variables: Temperatura de ambiente ($T_m$), Temperatura Inicial ($T_0$), Temperatura evaluada en el momento $n$ ($T_n$) y su respectivo tiempo ($t_n$).

### Frontend (Vue 3 + Vite + Clean Architecture)
Consumo del servicio expuesto, donde se simula la gráfica del decaimiento térmico y se tabulan los resultados. El frontend sigue estrictamente una estructura *Clean Architecture* organizada en:
- `src/domain`: Entidades puras y de datos desconectadas del entorno UI o HTTP (`CoolingItem`, `CoolingResult`).
- `src/application`: Casos de uso (`CalculateCooling`) y puertos (`CoolingRepository`). Contienen las reglas de negocio base o validaciones estructurales.
- `src/infrastructure`: Adaptadores. Contiene la forma en que el repositorio consume la API de Python Django (`HttpCoolingRepository`) usando mapeadores a dominios propios.
- `src/presentation`: Contiene los componentes visuales en `Vue`, el composable reaccionario (`useCoolingCalculator`) y la vista principal del dashboard.

---

## 📋 Requisitos previos

- [Docker](https://www.docker.com/) y Docker Compose v2.
- Node.js versión `22.x` o superior (solo si ejecutas el frontend por fuera de Docker Compose).

---

## 🚀 Despliegue con Docker (Modo Desarrollo)

Todo el proyecto (tanto frontend como backend) se levanta ejecutando:

```bash
docker compose -f docker-compose-desarrollo.yml up --build
```

**Accesos una vez levantado**:
- **Frontend SPA:** [http://localhost:5173](http://localhost:5173)
- **Backend API:** [http://localhost:8000/api/ley-enfriamiento/](http://localhost:8000/api/ley-enfriamiento/)

---

## 🧪 Pruebas Unitarias

El proyecto cuenta con testing para garantizar la exactitud en la lógica de dominio y matemáticas en ambas capas (backend y frontend).

### Backend (Pytest)
```bash
docker exec -it backend-container sh -c "cd /app/backend && DJANGO_SETTINGS_MODULE=config.settings.test pytest -v"
```

### Frontend (Vitest)
```bash
docker run --rm -v $(pwd)/frontend:/app -w /app node:22-alpine npx vitest run
```
*(Nota: Si ejecutas localmente sin el contenedor, simplemente usa `npm test` ó `npx vitest run` ubicándote dentro de `/frontend`).*

---

## 🔌 API REST (Backend)

La API acepta llamados por `POST` y `GET`. 
Rechaza aquellos datos que son inconsistentes con la realidad termodinámica (ejemplo, objetos inicialmente hirviendo que se enfrían mágicamente a una temperatura inferior al clima ambiente, o divisiones por cero en el logaritmo para el coeficiente `K` si un usuario trata de predecir o setear temperaturas idénticas en $t=0$).

### Parámetros HTTP 

| Variable | Descripción |
|---|---|
| `temperatura_medio_ambiente` | Temperatura del medio ambiente ($T_m$). |
| `temperatura_inicial` | Temperatura inicial del objeto ($T_0$). |
| `temperatura_momento_n` | Temperatura de muestra iterativa ($T_n$). |
| `tiempo_momento_n` | Minuto o instante en que se evaluó el parámetro anterior. |
| `tiempo_total` | **[Opcional]** Fija el límite graficado en minutos o instantes. Default: `60`. |
| `paso_tiempo` | **[Opcional]** Los saltos de instante que el modelo graficará a evaluar. Default: `3`. |

---

## 🎨 Diagrama del Flujo Visual (Frontend)

1. El usuario visualiza `CoolingView` a través del explorador. Se visualiza un panel estilo dashboard. 
2. A nivel del panel, el archivo `CoolingForm.vue` obtiene del usuario las 4 variables matemáticas requeridas.
3. El componente despacha el evento al composable `useCoolingCalculator.js`. 
4. El caso de uso valida, y si todo sale de maravilla, `HttpCoolingRepository` consume el servicio de Django.
5. El servidor Python retorna el valor de constante `K` obtenido analíticamente con Logaritmos y entrega el array de predicciones.
6. Se proyectan en pantalla `CoolingTable.vue` (visualizando los diferenciales de error) y `CoolingChart.vue` procesa la iteración mediante `Chart.js` comparando interactivamente el objeto vs el ambiente. 

---

### Responsabilidades / Exenciones
*Proyecto netamente académico creado como evaluación (Quiz 1) de resolución lógica-Matemática usando tecnologías SPA Backend.*
