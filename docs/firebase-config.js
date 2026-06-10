// ═══════════════════════════════════════════════════════════════
// CONFIGURACIÓN DE FIREBASE — FamiliaFinance XP
//
// Pasos (una sola vez, ~5 minutos — guía completa en FIREBASE-SETUP.md):
//   1) Entra a https://console.firebase.google.com y crea un proyecto.
//   2) Agrega una "App web" (icono </>) y copia aquí el objeto
//      firebaseConfig que te muestra Firebase.
//   3) En Authentication → Sign-in method, activa
//      "Correo electrónico/contraseña".
//   4) En Firestore Database, crea la base de datos y pega las reglas
//      de seguridad indicadas en FIREBASE-SETUP.md.
//
// Mientras este archivo tenga los valores "PEGA_AQUI...", la aplicación
// funciona en MODO LOCAL: el login opera igual, pero los datos solo se
// guardan en el navegador de cada uno (no se comparten).
// ═══════════════════════════════════════════════════════════════
window.FIREBASE_CONFIG = {
  apiKey: "PEGA_AQUI_TU_API_KEY",
  authDomain: "PEGA_AQUI_TU_PROYECTO.firebaseapp.com",
  projectId: "PEGA_AQUI_TU_PROYECTO",
  storageBucket: "PEGA_AQUI_TU_PROYECTO.appspot.com",
  messagingSenderId: "PEGA_AQUI",
  appId: "PEGA_AQUI"
};
