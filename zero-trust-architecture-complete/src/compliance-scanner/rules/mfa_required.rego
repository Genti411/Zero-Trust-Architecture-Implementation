package zta

violation["MFA required"] {
  input.role == "admin"
  not input.mfa_enabled
}
