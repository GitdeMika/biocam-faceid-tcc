# README.md para o Projeto de API de Biometria

## Visão Geral do Projeto

Este projeto implementa um **sistema de autenticação biométrica** usando uma webcam, aproveitando tecnologias como **Flask**, **MediaPipe**, **MySQL**, **TensorFlow**, **HTML**, **CSS** e **JavaScript**. A API captura características faciais em tempo real através da webcam e as processa para verificação de usuários, oferecendo uma solução moderna para controle de acesso seguro.

## Funcionalidades

- **Integração com Webcam**: Utiliza a webcam do usuário para capturar vídeo em tempo real para análise biométrica.
- **Reconhecimento Facial**: Emprega MediaPipe para detecção e reconhecimento precisos de marcos faciais.
- **Aprendizado de Máquina**: Integra TensorFlow para treinar e implantar modelos de aprendizado de máquina que aumentam a precisão biométrica.
- **Gerenciamento de Banco de Dados**: Usa MySQL para armazenar dados de usuários e templates biométricos com segurança.
- **Interface Web Responsiva**: Construída com HTML, CSS e JavaScript para garantir uma experiência amigável em diversos dispositivos.

## Tecnologias Utilizadas

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Aprendizado de Máquina**: TensorFlow
- **Processamento Biométrico**: MediaPipe
- **Banco de Dados**: MySQL

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/biometric-api.git
   cd biometric-api