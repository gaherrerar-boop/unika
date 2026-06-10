# Sincronización en la nube — FamiliaFinance XP

La app ya está conectada a Supabase y **no requiere configuración
adicional**. Ambos usuarios (gherrera y Danita) ven y editan los mismos
datos en tiempo real desde cualquier dispositivo.

## Cómo funciona

- **Autenticación:** las credenciales de la app están respaldadas en
  Supabase Auth (proyecto `gaherrerar-boop's Project`, organización
  gherrerayms) como `gherrera@familiafinance-xp.cl` y
  `danita@familiafinance-xp.cl` (correos internos, no reales).
- **Datos compartidos:** viven en la tabla `familiafinance` (una fila por
  tipo de dato: ingresos, gastos, listas, configuración, etc.).
- **Tiempo real:** la app está suscrita a los cambios de esa tabla; lo
  que registra un usuario aparece en el otro dispositivo en segundos.
- **Seguridad:** la tabla tiene Row Level Security: solo usuarios
  autenticados pueden leer o escribir. La clave que aparece en
  `supabase-config.js` es la clave publicable (pública por diseño).
- **Sin conexión:** si la nube no responde, la app sigue funcionando en
  modo local y lo indica en la barra de tareas.

## Indicadores en la barra de tareas

- `☁️ Sincronizado` — conectado, datos compartidos.
- `⚠️ Sin conexión` — error temporal de red; se guarda localmente.
- `💾 Modo local` — sin configuración de nube.

## Nota de seguridad

Las contraseñas de la familia están escritas dentro del código y este
repositorio es público: cualquiera que lea el código podría conocerlas y,
con ellas, entrar a la app y ver los datos. No reutilices estas
contraseñas en otros servicios.
