# Backlog - Onboarding 

> Repositório: documentação do backlog, épicos, critérios e riscos do projeto de onboarding.

---

## Tabela Resumida

Histórias priorizadas pelo método **MoSCoW** (Must/Should).

| ID | História de Usuário | Prioridade | Status | Sprint |
| --- | --- | --- | --- | --- |
| **US01** | Como cliente, quero preencher um formulário de cadastro para iniciar o onboarding. | **Must** | To Do | Sprint 1 |
| **US02** | Como sistema, quero validar os dados do formulário no backend para garantir consistência. | **Must** | To Do | Sprint 1 |
| **US03** | Como sistema, quero criar automaticamente o cliente na plataforma via N8N após validação. | **Must** | To Do | Sprint 1 |
| **US07** | Como cliente, quero ser notificado em caso de falha no cadastro para saber como proceder. | **Must** | To Do | Sprint 1 |
| **US04** | Como sistema, quero replicar o cadastro do cliente no CRM para centralizar informações comerciais. | **Should** | To Do | Sprint 2 |
| **US05** | Como sistema, quero enviar e-mail de boas-vindas automaticamente ao cliente cadastrado. | **Should** | To Do | Sprint 2 |
| **US06** | Como time comercial, quero que a reunião seja agendada automaticamente para agilizar follow-up. | **Should** | To Do | Sprint 2 |
| **US08** | Como suporte, quero receber alertas de falhas no fluxo para atuar rapidamente. | **Should** | To Do | Sprint 2 |

---

## Tabela Detalhada

| Título | ID | Descrição | Prioridade | Sprint Prevista | Critérios de Aceite Resumidos | Links / Protótipos | Dependências / Observações |
| --- | ---: | --- | --- | ---: | --- | --- | --- |
| Formulário de Cadastro | US01 | Como cliente, quero preencher um formulário de cadastro para iniciar o onboarding, garantindo coleta correta dos dados essenciais. | Must | Sprint 1 | Todos os campos obrigatórios validados; mensagem de sucesso exibida; UX responsiva. | `prototipos/Formulario-Figma.pdf` | Integração com backend para validação; validações front-end. |
| Validação Backend | US02 | Como sistema, quero validar os dados do formulário no backend para impedir cadastros inválidos. | Must | Sprint 1 | Regras de validação aplicadas; entradas inválidas rejeitadas com mensagens claras; logs registrados. | — | Regras de negócio definidas; testes automatizados. |
| Criação de Cliente na plataforma | US03 | Como sistema, quero criar automaticamente o cliente na plataforma via N8N após validação. | Must | Sprint 1 | Cliente criado corretamente na Runy; respostas de erro tratadas. | — | API Runy disponível; credenciais válidas; fluxo N8N configurado. |
| Notificação de Falha (Cliente) | US07 | Como cliente, quero ser notificado em caso de falha no cadastro para saber como proceder. | Must | Sprint 1 | Notificação enviada ao cliente com instruções; fallback de retry definido. | — | Integração N8N; servidor de e-mail configurado. |
| Criação de Cliente no CRM | US04 | Como sistema, quero replicar o cadastro do cliente no CRM para centralizar informações comerciais. | Should | Sprint 2 | Cliente criado no CRM com mapeamento correto de campos. | — | API CRM disponível; mapeamento de campos definido. |
| E-mail de Boas-vindas | US05 | Como sistema, quero enviar e-mail de boas-vindas automaticamente ao cliente cadastrado. | Should | Sprint 2 | E-mail enviado com template aprovado; link de próximos passos incluso. | — | Template aprovado; servidor de envio configurado. |
| Agendamento de Reunião | US06 | Como time comercial, quero que a reunião seja agendada automaticamente após cadastro do cliente. | Should | Sprint 2 | Evento criado no calendário; confirmação enviada por e-mail. | — | Integração com calendário (Google/Office 365); regras de disponibilidade. |
| Alertas de Falha (Suporte) | US08 | Como suporte, quero receber alertas de falhas no fluxo para atuar rapidamente. | Should | Sprint 2 | Notificação interna enviada com detalhes da falha e cliente afetado; painel de incidentes atualizado. | — | Integração com sistema de alertas/CRM; dashboards configurados. |

---

## Épicos e Tasks Detalhadas

### Épico 1 – Onboarding do Cliente
**Objetivo:** Garantir que o cliente consiga se cadastrar e que o sistema valide os dados corretamente.

| ID | User Story | Prioridade | Status | Sprint | Tasks Detalhadas |
| --- | --- | --- | --- | --- | --- |
| US01 | Como cliente, quero preencher um formulário de cadastro para iniciar o onboarding. | Must | To Do | Sprint 1 | - Criar layout do formulário<br>- Definir campos obrigatórios (nome, e-mail, empresa, telefone)<br>- Criar botão de envio<br>- Validar preenchimento no front-end |
| US02 | Como sistema, quero validar os dados do formulário no backend para garantir consistência. | Must | To Do | Sprint 1 | - Definir regras de validação (e-mail válido, campos obrigatórios)<br>- Implementar validação no Laravel<br>- Simular retorno de validação (sucesso/falha)<br>- Registrar logs de tentativas de cadastro |

### Épico 2 – Integração e Automação
**Objetivo:** Criar e integrar o cliente automaticamente na plataforma e no CRM via N8N.

| ID | User Story | Prioridade | Status | Sprint | Tasks Detalhadas |
| --- | --- | --- | --- | --- | --- |
| US03 | Como sistema, quero criar o cliente automaticamente na plataforma via N8N após validação. | Must | To Do | Sprint 1 | - Mapear campos do formulário para API plataforma<br>- Criar fluxo de automação no N8N<br>- Implementar tratamento de erros e retries<br>- Testes de integração (success/failure) |
| US04 | Como sistema, quero replicar o cadastro do cliente no CRM para centralizar informações comerciais. | Should | To Do | Sprint 2 | - Mapear dados necessários para CRM<br>- Criar fluxo de integração com CRM via N8N<br>- Validar registro do cliente no CRM<br>- Criar logs/alertas para falhas |

### Épico 3 – Comunicação e Notificações
**Objetivo:** Garantir que clientes e suporte sejam notificados corretamente sobre o status do cadastro.

| ID | User Story | Prioridade | Status | Sprint | Tasks Detalhadas |
| --- | --- | --- | --- | --- | --- |
| US05 | Como sistema, quero enviar e-mail de boas-vindas automaticamente ao cliente cadastrado. | Should | To Do | Sprint 2 | - Criar template de e-mail (marketing + instruções)<br>- Integrar envio via N8N<br>- Simular envio e verificar entrega |
| US07 | Como cliente, quero ser notificado em caso de falha no cadastro para saber como proceder. | Must | To Do | Sprint 1 | - Criar alertas visuais no protótipo<br>- Simular envio de e-mail de erro ao cliente<br>- Definir mensagem de instrução para próxima ação |
| US08 | Como suporte, quero receber alertas de falhas no fluxo para atuar rapidamente. | Should | To Do | Sprint 2 | - Criar notificação interna para suporte<br>- Detalhar tipo de falha e cliente afetado<br>- Simular painel de alertas de falha |

### Épico 4 – Agendamento Automático
**Objetivo:** Garantir que o time comercial receba reuniões agendadas automaticamente após cadastro do cliente.

| ID | User Story | Prioridade | Status | Sprint | Tasks Detalhadas |
| --- | --- | --- | --- | --- | --- |
| US06 | Como time comercial, quero que a reunião seja agendada automaticamente para agilizar follow-up. | Should | To Do | Sprint 2 | - Criar integração com agenda do time comercial via N8N<br>- Definir regras de disponibilidade e buffer times<br>- Simular agendamento automático<br>- Notificar participante e criar evento no calendário |

---

## Red Flags / Pontos Críticos

1. **Dependências Técnicas**  
   - Integração com APIs externas (plataforma, CRM) e configuração segura de autenticação.  
   - Envio de e-mails automatizados e integração com N8N.  
   - **Mitigação:** Confirmar disponibilidade das APIs e credenciais antes da Sprint; realizar testes de conexão preliminares e validar ambientes (sandbox/produção).

2. **Critérios de Sucesso**  
   - Todos os dados válidos devem criar registros corretos nas plataformas (plataforma e CRM).  
   - Notificações (e-mails ou alertas internos) devem ser enviadas corretamente e sem perdas.  
   - **Mitigação:** Criar testes automatizados, cenários de integração e testes de entrega de e-mail (SPF/DKIM/DMARC verificados).

3. **Notas de Priorização**  
   - **MVP (Sprint 1):** foco em cadastro, validação backend e notificações de falha.  
   - **Incrementos (Sprint 2):** integração com CRM, envio de e-mail de boas-vindas e agendamento automático.  
   - **Mitigação:** Revisar prioridades antes do planejamento da Sprint; definir critérios de corte para MVP.

4. **Flexibilidade do Backlog**  
   - User Stories podem ser refinadas após a primeira Sprint para incluir campos extras, personalizações de template ou melhorias de UX.  
   - **Mitigação:** Agendar sessões de refinamento regulares e manter histórico de mudanças no GitHub para rastreabilidade.

---

## Observações finais / Próximos passos sugeridos

- Vincular cada US a **issues** no GitHub (quando iniciar desenvolvimento) para rastrear tarefas técnicas e dependências.  
- Preparar ambiente de testes (sandbox) para plataforma e CRM antes da Sprint 1.  
- Validar templates de e-mail e configurações de entrega com time de infraestrutura.  
- Criar Project Board (Kanban) para Sprint 1 com colunas: Backlog / To Do / In Progress / Done.

