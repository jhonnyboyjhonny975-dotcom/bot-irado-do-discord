# 🤖 Bot Classificador de Imagens — Discord

> Bot para Discord que usa Inteligência Artificial para identificar e classificar imagens enviadas pelos usuários!

---

## 📝 Descrição

Este bot se conecta ao Discord e utiliza um modelo treinado de aprendizado de máquina para reconhecer o conteúdo de imagens. O usuário envia uma imagem com o comando `$check` e recebe em segundos a classificação feita pela IA.

### Como funciona:
1. 📥 O usuário envia uma imagem junto com o comando `$check`
2. 💾 O bot salva a imagem temporariamente
3. 🧠 O arquivo é passado para o modelo (`keras_model.h5`) que analisa as características visuais
4. 🏷️ O modelo retorna a classe correspondente e o bot responde com o resultado
5. 🧹 O arquivo é removido automaticamente depois do processamento

### Comandos disponíveis:
| Comando | O que faz |
|---|---|
| `$hello` | Cumprimenta o bot 🖐️ |
| `$heh [número]` | Repete "he" várias vezes 😄 |
| `$enviar` | Salva a imagem enviada na pasta `save/` 💾 |
| `$check` | Classifica a imagem com o modelo de IA 🔍 |

---

## 🚀 Como executar

### Pré-requisitos
- Python 3.8 ou superior
- Conta de bot no Discord e token de acesso

### Instalação
```bash
# Clone ou baixe este repositório
cd nome-da-pasta

# Instale as dependências
pip install discord.py tensorflow pillow
