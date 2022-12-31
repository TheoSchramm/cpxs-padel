def __main__():
    from cv2 import VideoCapture, CAP_PROP_FRAME_HEIGHT, CAP_PROP_FRAME_WIDTH, VideoWriter_fourcc, imshow, waitKey, VideoWriter, destroyAllWindows
    from os import makedirs, path
    from pathlib import Path
    from datetime import datetime

    # Define o obj de captura de video e suas proporções
    cap = VideoCapture(0)
    width= int(cap.get(CAP_PROP_FRAME_WIDTH))
    height= int(cap.get(CAP_PROP_FRAME_HEIGHT))
    # Define o codec do obj de armazenamento de video
    fourcc = VideoWriter_fourcc('m', 'p', '4', 'v')

    # Lista que servirá como cache dos últimos 900 frames
    frame_list = []
    frame_limit = 30*30

    # Define o diretório padrão para as gravações
    default_path = f'{Path.home()}\\Downloads\\CV2'
    # Caso não tenha tal diretório, cria-se um
    if not path.exists(default_path):
        makedirs(default_path)

    while True:
        # Captura e mostra o frame atual
        ret, frame = cap.read()

        frame_list.append(frame)
        if len(frame_list) > frame_limit:
            frame_list.pop(0)

        imshow(f'Pressione ESC para fechar ou R para gravar os ultimos 30 segundos', frame)
        
        # Um modo de parar a execução o programa
        if waitKey(1) & 0xFF == 27: #esc
            break

        # Salva os últimos 900 frames capturados
        if waitKey(1) & 0xFF in [ord('r'),ord('R')]:
            print('>> Sys: Gravando últimos 30 segundos')
            out = VideoWriter(f'{default_path}//{datetime.now().strftime("%d-%m-%y-%H-%M-%S")}.mp4', fourcc, 30.0, (width, height))
            for frame in frame_list:
                out.write(frame)
            out.release()

    # Fecha todas as janelas abertas
    destroyAllWindows()

    # É necessário liberar o acesso desse dispositvo para evitar conflitos e ganhar + memória
    cap.release()

# É sempre bom fazer isso para evitar o script de rodar quando for importado para outros códigos
if __name__ == '__main__':
    __main__()
