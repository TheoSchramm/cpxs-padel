# __⏪ reWinder__
  Um programa feito em Python que regularmente captura os últimos 30 segundos da sua webcam, e ao pressionar de um botão transforma esses últimos 30 segundos em um arquivo mp4 para você poder reviver o momento!<br>

# __👨‍💻 Como funciona__
  Este código define uma classe "VideoRecorder" que usa a biblioteca OpenCV para capturar o vídeo da câmera padrão e exibi-lo em uma janela. Ele também permite que o usuário grave os últimos 30 segundos de vídeo clicando com o botão direito do mouse na janela e salva o vídeo gravado na pasta Downloads/CV2 do usuário com um nome de arquivo baseado na data e hora atuais (Formatação ISO). <br> <br>
  O código usa a classe cv2.VideoCapture para acessar a câmera, a classe cv2.VideoWriter para salvar o vídeo gravado e a função cv2.setMouseCallback para detectar quando o usuário clica com o botão direito do mouse na janela. Ele também usa o módulo OS para verificar se a pasta de destino padrão existe e criá-la caso contrário, o módulo datetime para gerar o nome do arquivo com base na data e hora atuais e o pathlib para obter o diretório padrão do usuário.

# __🤔 Como utilizar?__
1. Baixe e execute o arquivo PYw<br>
2. Se sua webcam não estiver aparecendo, verifique seu dispositivo padrão de captura de vídeo<br>
3. Com a janela do aplicato aberta, dê um clique com o botão direito do seu mouse<br>
4. Pronto, seu clipe já está disponível, verifique sua pasta Downloads<br>

# __📝 Falta terminar__
  - Transcrever todo o código para C#<br>
  - Conseguir uma câmera externa para continuar o código<br>
  - Capturar audio<br>
  - ?<br>
  - profit<br>
