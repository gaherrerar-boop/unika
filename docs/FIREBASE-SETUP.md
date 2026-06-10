# Configurar Firebase para FamiliaFinance XP

Con esta configuración, **gherrera** y **Danita** verán y editarán los
mismos datos en tiempo real desde cualquier dispositivo.

Solo se hace una vez y toma unos 5 minutos. Hasta entonces, la app
funciona en "Modo local" (cada navegador guarda sus propios datos).

## 1. Crear el proyecto

1. Entra a <https://console.firebase.google.com> con tu cuenta de Google.
2. **Agregar proyecto** → nombre: `familiafinance` (o el que quieras) →
   puedes desactivar Google Analytics → **Crear proyecto**.

## 2. Registrar la app web y copiar la configuración

1. En la pantalla principal del proyecto, pulsa el icono **`</>`** (Web).
2. Apodo: `FamiliaFinance XP` → **Registrar app** (no marques Hosting).
3. Firebase te mostrará un bloque `const firebaseConfig = { ... }`.
4. Copia esos valores dentro de `docs/firebase-config.js` de este
   repositorio, reemplazando los `PEGA_AQUI...`:

```js
window.FIREBASE_CONFIG = {
  apiKey: "AIza...",
  authDomain: "familiafinance.firebaseapp.com",
  projectId: "familiafinance",
  storageBucket: "familiafinance.appspot.com",
  messagingSenderId: "1234567890",
  appId: "1:1234567890:web:abc123"
};
```

Puedes editarlo directamente en GitHub (abrir el archivo → lápiz ✏️ →
Commit). GitHub Pages se republicará solo.

## 3. Activar Authentication

1. Menú lateral → **Compilación → Authentication** → **Comenzar**.
2. Pestaña **Sign-in method** → habilita **Correo electrónico/contraseña**
   → Guardar.

No necesitas crear los usuarios a mano: la primera vez que `gherrera` o
`Danita` inicien sesión en la app, sus cuentas se registran solas en
Firebase Auth (como `gherrera@familiafinance-xp.cl` y
`danita@familiafinance-xp.cl`, correos internos de la app).

## 4. Crear Firestore y pegar las reglas

1. Menú lateral → **Compilación → Firestore Database** → **Crear base de
   datos** → modo **producción** → ubicación: `southamerica-east1` (o la
   más cercana) → **Habilitar**.
2. Pestaña **Reglas**, reemplaza todo por:

```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /familiafinance/{docId} {
      allow read, write: if request.auth != null;
    }
  }
}
```

3. **Publicar**.

Esto permite leer/escribir los datos compartidos solo a usuarios
autenticados (es decir, solo gherrera y Danita).

## 5. Listo

Abre la app publicada, inicia sesión y verifica que en la barra de tareas
aparezca **☁️ Sincronizado**. Lo que registre un usuario aparecerá
automáticamente en la pantalla del otro.

## Nota de seguridad

Las contraseñas de la familia están escritas dentro del código de la app
(así fue solicitado) y el repositorio es público. Cualquiera que lea el
código podría conocerlas. No reutilices estas contraseñas en otros
servicios. Si quieres más privacidad, haz el repositorio privado
(GitHub Pages privado requiere plan de pago) o pide cambiar el esquema de
autenticación.
