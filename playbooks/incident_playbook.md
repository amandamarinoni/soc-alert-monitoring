# Playbook: Resposta a brute-force SSH

## Objetivo
Mitigar e investigar tentativas de brute-force SSH.

## Detecção
- Sinais: múltiplas falhas de autenticação em curto período vindas do mesmo IP.

## Ações Imediatas
1. Bloquear IP no firewall / security group.
2. Desativar conta(s) comprometidas temporariamente.
3. Rotina de coleta: copiar logs, salvar timestamps, capturar processo em execução.
4. Implementar proteção: Fail2ban, MFA, redução de superfície (desabilitar root login).
5. Escalonamento: notificar equipe e registrar incidente no sistema de tickets.

## Pós-incidente
- Fazer análise forense, reavaliar regras de firewall, atualizar playbook.
