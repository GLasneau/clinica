# Clinica API

API Django para gerenciamento de uma clinica medica, dividida em 3 apps:

- **pacientes** — cadastro de pacientes
- **medicos** — cadastro de medicos
- **consultas** — agendamento de consultas, relacionando paciente e medico (ForeignKey)

## Como rodar

```bash
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

- Admin: http://127.0.0.1:8000/admin/
- Listagem de consultas (JSON): http://127.0.0.1:8000/consultas/

## Models

- `Paciente`: nome, data_nascimento, telefone, ativo
- `Medico`: nome, especialidade, crm, anos_experiencia
- `Consulta`: paciente (FK), medico (FK), data_hora, observacoes, realizada
