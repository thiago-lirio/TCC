import imgaug as ia
import imgaug.augmenters as iaa
import time
from os import listdir
import psutil
import cv2
import numpy as np

class Image_Processing():

    def __init__(self, dataset, pastaSaida, quantidade):
        super().__init__()
        self.dataset = dataset
        self.pastaSaida = pastaSaida
        self.quantidade = quantidade


        self.arquivos = [f for f in listdir(dataset)]
        print(self.arquivos)
        ia.seed(1)


    def ruidoGaussiano(self, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            ##start = time.time()
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.AdditiveGaussianNoise(
                        loc= ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5),
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-Ruido.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])
                ##end = time.time()
                ##print(start - end)
                print (psutil.virtual_memory()[2])


    def cisalhamento(self, minCisalhamento, maxCisalhamento):
        for self.imagem in self.arquivos:
            start = time.time()
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        shear=(minCisalhamento, maxCisalhamento)
                    )

                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-Cis.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])
                end = time.time()
                #print(start - end)
                print(psutil.virtual_memory()[2])

    def corte(self, relacaoCorte):
        for self.imagem in self.arquivos:
            start = time.time()
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Crop(percent=(0, relacaoCorte))
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-Corte.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])
                end = time.time()
                #print(start - end)
                print(psutil.virtual_memory()[2])

    def cisalhamentoRuidoGaussiano(self, minCisalhamento, maxCisalhamento, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5),

                    iaa.Affine(
                        shear=(minCisalhamento, maxCisalhamento)
                    )

                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-CisRuidoGaussiano.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def corteRuidoGaussiano(self, relacaoCorte, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5),

                    iaa.Crop(percent=(0, relacaoCorte))
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-CorteRuidoGaussiano.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])
                cv2.waitKey(1000)

    def flipVertical(self):
        for self.imagem in self.arquivos:
            start = time.time()
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Flipud()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-FlipVert.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])
                end = time.time()
                #print(start - end)
                print(psutil.virtual_memory()[2])

    def flipVerticalRuidoGaussiano(self, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Flipud(),
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5)
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-FlipVertRuido.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])
                cv2.waitKey(1000)

    def flipVerticalCisalhamento(self, minCisalhamento, maxCisalhamento):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Flipud(),
                    iaa.Affine(
                        shear=(minCisalhamento, maxCisalhamento)
                    )
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-FlipVertCis.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])
                cv2.waitKey(1000)

    def flipVerticalCorte(self, relacaoCorte):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Flipud(),
                    iaa.Crop(percent=(0, relacaoCorte))

                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-FlipVertCorte.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])
                cv2.waitKey(1000)

    def flipVerticalCisalhamentoRuidoGaussiano(self, minCisalhamento, maxCisalhamento, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Flipud(),
                    iaa.Affine(
                        shear=(minCisalhamento, maxCisalhamento)
                    ),
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5)
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-FlipVertCisRuido.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])
                cv2.waitKey(1000)

    def flipVerticalCorteRuidoGaussiano(self, relacaoCorte, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Flipud(),
                    iaa.Crop(percent=(0, relacaoCorte)),
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5)

                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-FLipVertCorteRuido.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])
                cv2.waitKey(1000)

    def flipHorizontal(self):
        for self.imagem in self.arquivos:
            start = time.time()
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Fliplr()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-FlipHoriz.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])
                end = time.time()
                print(psutil.virtual_memory()[2])

    def flipHorizontalRuidoGaussiano(self, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5),
                    iaa.Fliplr()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                print(self.pastaSaida)
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-FlipHorizRuido.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])
                cv2.waitKey(1000)

    def flipHorizontalCisalhamento(self, minCisalhamento, maxCisalhamento):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Fliplr(),
                    iaa.Affine(
                        shear=(minCisalhamento, maxCisalhamento)
                    )
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-FlipHorizCis.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])
                cv2.waitKey(1000)

    def flipHorizontalCorte(self, relacaoCorte):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Fliplr(),
                    iaa.Crop(percent=(0, relacaoCorte))

                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-FlipHorizCorte.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])
                cv2.waitKey(1000)

    def flipHorizontalCisalhamentoRuidoGaussiano(self, minCisalhamento, maxCisalhamento, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Fliplr(),
                    iaa.Affine(
                        shear=(minCisalhamento, maxCisalhamento)
                    ),
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5)
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-FlipHorizCisRuido.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])
                cv2.waitKey(1000)

    def flipHorizontalCorteRuidoGaussiano(self, relacaoCorte, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Fliplr(),
                    iaa.Crop(percent=(0, relacaoCorte)),
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5)

                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-FlipHorizCorteRuido.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])
                cv2.waitKey(1000)

    def flipHorizontalVertical(self):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Fliplr(),
                    iaa.Flipud()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-FlipHorizVert.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])
                cv2.waitKey(1000)

    def flipHorizontalVerticalRuidoGaussiano(self, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5),
                    iaa.Fliplr(),
                    iaa.Flipud()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-FlipHorizVertRuido.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])
                cv2.waitKey(1000)

    def flipHorizontalVerticalCisalhamento(self, minCisalhamento, maxCisalhamento):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Fliplr(),
                    iaa.Affine(
                        shear=(minCisalhamento, maxCisalhamento)
                    ),
                    iaa.Flipud()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-FlipHorizVertCis.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])
                cv2.waitKey(1000)

    def flipHorizontalVerticalCorte(self, relacaoCorte):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Fliplr(),
                    iaa.Crop(percent=(0, relacaoCorte)),
                    iaa.Flipud()

                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-FlipHorizVertCorte.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])
                cv2.waitKey(1000)

    def flipHorizontalVerticalCisalhamentoRuidoGaussiano(self, minCisalhamento, maxCisalhamento, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Fliplr(),
                    iaa.Affine(
                        shear=(minCisalhamento, maxCisalhamento)
                    ),
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5),
                    iaa.Flipud()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-FlipHorizVertCisRuido.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])
                cv2.waitKey(1000)

    def flipHorizontalVerticalCorteRuidoGaussiano(self, relacaoCorte, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Fliplr(),
                    iaa.Crop(percent=(0, relacaoCorte)),
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5),
                    iaa.Flipud()

                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-FlipHorizVertCorteRuido.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])
                cv2.waitKey(1000)

    def rotacao(self, MinRot, MaxRot):
        for self.imagem in self.arquivos:
            start=time.time()
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        rotate=(MinRot, MaxRot)
                    )
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-Rot.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])
                end = time.time()
                #print(start - end)
                print(psutil.virtual_memory()[2])

    def rotacaoRuidoGaussiano(self, MinRot, MaxRot, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            start = time.time()
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])

            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        rotate=(MinRot, MaxRot)
                    ),
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5)
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-RotRuido.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])
                end = time.time()
                print(start - end)

    def rotacaoCisalhamento(self, MinRot, MaxRot, minCisalhamento, maxCisalhamento):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        rotate=(MinRot, MaxRot),
                        shear=(minCisalhamento, maxCisalhamento)
                    ),
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-RotCis.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def rotacaoCorte(self, MinRot, MaxRot, relacaoCorte):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        rotate=(MinRot, MaxRot),
                    ),
                    iaa.Crop(percent=(0, relacaoCorte))
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-RotCorte.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def rotacaoCisalhamentoRuidoGaussiano(self, MinRot, MaxRot, minCisalhamento, maxCisalhamento, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        rotate=(MinRot, MaxRot),
                        shear=(minCisalhamento, maxCisalhamento)
                    ),
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5)
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-RotCisRuido.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def rotacaoCorteRuidoGaussiano(self, MinRot, MaxRot, relacaoCorte, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        rotate=(MinRot, MaxRot),
                    ),
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5),
                    iaa.Crop(percent=(0, relacaoCorte))
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-RotCorteRuido.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def rotacaoFlipVertical(self, MinRot, MaxRot):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        rotate=(MinRot, MaxRot)
                    ),
                    iaa.Flipud()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-RotFlipVert.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])
                cv2.waitKey(1000)

    def rotacaoFlipVerticalRuidoGaussiano(self, MinRot, MaxRot, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        rotate=(MinRot, MaxRot)
                    ),
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5),
                    iaa.Flipud()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-RotFlipVertRuido.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])
                cv2.waitKey(1000)

    def rotacaoFlipVerticalCisalhamento(self, MinRot, MaxRot, minCisalhamento, maxCisalhamento):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        rotate=(MinRot, MaxRot),
                        shear=(minCisalhamento, maxCisalhamento)
                    ),
                    iaa.Flipud()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-RotFlipVertCis.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])
                cv2.waitKey(1000)

    def rotacaoFlipVerticalCorte(self, MinRot, MaxRot, relacaoCorte):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        rotate=(MinRot, MaxRot),
                    ),
                    iaa.Crop(percent=(0, relacaoCorte)),
                    iaa.Flipud()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-RotFlipVertCorte.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])
                cv2.waitKey(1000)

    def rotacaoFlipVerticalCisalhamentoRuidoGaussiano(self, MinRot, MaxRot, minCisalhamento, maxCisalhamento, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        rotate=(MinRot, MaxRot),
                        shear=(minCisalhamento, maxCisalhamento)
                    ),
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5),
                    iaa.Flipud()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-RotFlipVertCisRuido.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def rotacaoFlipVerticalCorteRuidoGaussiano(self, MinRot, MaxRot, relacaoCorte, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        rotate=(MinRot, MaxRot),
                    ),
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5),
                    iaa.Crop(percent=(0, relacaoCorte)),
                    iaa.Flipud()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-RotFlipVertCorteRuido.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def rotacaoFlipHorizontal(self, MinRot, MaxRot):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        rotate=(MinRot, MaxRot)
                    ),
                    iaa.Fliplr()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-RotFlipHoriz.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])

    def rotacaoFlipHorizontalRuidoGaussiano(self, MinRot, MaxRot, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        rotate=(MinRot, MaxRot)
                    ),
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5),
                    iaa.Fliplr()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-RotFlipHorizRuido.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def rotacaoFlipHorizontalCisalhamento(self, MinRot, MaxRot, minCisalhamento, maxCisalhamento):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        rotate=(MinRot, MaxRot),
                        shear=(minCisalhamento, maxCisalhamento)
                    ),
                    iaa.Fliplr()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-RotFlipHorizCis.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def rotacaoFlipHorizontalCorte(self, MinRot, MaxRot, relacaoCorte):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        rotate=(MinRot, MaxRot),
                    ),
                    iaa.Crop(percent=(0, relacaoCorte)),
                    iaa.Fliplr()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-RotFlipHorizCorte.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def rotacaoFlipHorizontalCisalhamentoRuidoGaussiano(self, MinRot, MaxRot, minCisalhamento, maxCisalhamento, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        rotate=(MinRot, MaxRot),
                        shear=(minCisalhamento, maxCisalhamento)
                    ),
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5),
                    iaa.Fliplr()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-RotFlipHorizCisRuido.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def rotacaoFlipHorizontalCorteRuidoGaussiano(self, MinRot, MaxRot, relacaoCorte, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        rotate=(MinRot, MaxRot),
                    ),
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5),
                    iaa.Crop(percent=(0, relacaoCorte)),
                    iaa.Fliplr()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-RotFlipHorizCorteRuido.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def rotacaoFlipHorizontalVertical(self,MinRot, MaxRot):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Fliplr(),
                    iaa.Affine(
                        rotate=(MinRot, MaxRot),
                    ),
                    iaa.Flipud()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-RotFlipHorizVert.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def rotacaoFlipHorizontalVerticalRuidoGaussiano(self, MinRot, MaxRot, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        rotate=(MinRot, MaxRot)
                    ),
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5),
                    iaa.Fliplr(),
                    iaa.Flipud()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-RotFlipHorizVertRuido.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def rotacaoFlipHorizontalVerticalCisalhamento(self, MinRot, MaxRot, minCisalhamento, maxCisalhamento):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        rotate=(MinRot, MaxRot),
                        shear=(minCisalhamento, maxCisalhamento)
                    ),
                    iaa.Fliplr(),
                    iaa.flipud()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-RotFlipHorizVertCisalhamento.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def rotacaoFlipHorizontalVerticalCorte(self, MinRot, MaxRot, relacaoCorte):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        rotate=(MinRot, MaxRot),
                    ),
                    iaa.Crop(percent=(0, relacaoCorte)),
                    iaa.Fliplr(),
                    iaa.Flipud()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-RotFlipHorizVertCorte.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def rotacaoFlipHorizontalVerticalCisalhamentoRuidoGaussiano(self, MinRot, MaxRot, minCisalhamento, maxCisalhamento, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        rotate=(MinRot, MaxRot),
                        shear=(minCisalhamento, maxCisalhamento)
                    ),
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5),
                    iaa.Flipud(),
                    iaa.Fliplr()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-RotFlipHorizVertCisRuido.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def rotacaoFlipHorizontalVerticalCorteRuidoGaussiano(self, MinRot, MaxRot, relacaoCorte, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        rotate=(MinRot, MaxRot),
                    ),
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5),
                    iaa.Crop(percent=(0, relacaoCorte)),
                    iaa.Flipud(),
                    iaa.Fliplr()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-RotFlipHorizVertCorteRuido.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def escala(self, valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        scale={
                            "x": (valor_decimal_min_escX, valor_decimal_max_escX),
                            "y": (valor_decimal_min_escY, valor_decimal_max_escY)
                        }
                    )
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-Esc.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def escalaRuidoGaussiano(self, valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        scale={
                            "x": (valor_decimal_min_escX, valor_decimal_max_escX),
                            "y": (valor_decimal_min_escY, valor_decimal_max_escY)
                        }),
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5)
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-EscRuido.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])



    def escalaCisalhamento(self, valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY, minCisalhamento, maxCisalhamento):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        scale={
                            "x": (valor_decimal_min_escX, valor_decimal_max_escX),
                            "y": (valor_decimal_min_escY, valor_decimal_max_escY)
                        },
                        shear=(minCisalhamento, maxCisalhamento)
                    )
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-EscCis.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def escalaCorte(self, valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY, relacaoCorte):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        scale={
                            "x": (valor_decimal_min_escX, valor_decimal_max_escX),
                            "y": (valor_decimal_min_escY, valor_decimal_max_escY)
                        }
                    ),
                    iaa.Crop(percent=(0, relacaoCorte))
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-EscCorte.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def escalaCisalhamentoRuidoGaussiano(self, valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY, minCisalhamento, maxCisalhamento, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        scale={
                            "x": (valor_decimal_min_escX, valor_decimal_max_escX),
                            "y": (valor_decimal_min_escY, valor_decimal_max_escY)
                        },
                        shear=(minCisalhamento, maxCisalhamento)
                    ),
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5)
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-EscCisRuido.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def escalaCorteRuidoGaussiano(self, valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY, relacaoCorte, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        scale={
                            "x": (valor_decimal_min_escX, valor_decimal_max_escX),
                            "y": (valor_decimal_min_escY, valor_decimal_max_escY)
                        }
                    ),
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5),
                    iaa.Crop(percent=(0, relacaoCorte))
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-EscCorteRuido.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def escalaFlipVertical(self, valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        scale={
                            "x": (valor_decimal_min_escX, valor_decimal_max_escX),
                            "y": (valor_decimal_min_escY, valor_decimal_max_escY)
                        }
                    ),
                    iaa.Flipud()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-EscFlipVert.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def escalaFlipVerticalRuidoGaussiano(self, valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        scale={
                            "x": (valor_decimal_min_escX, valor_decimal_max_escX),
                            "y": (valor_decimal_min_escY, valor_decimal_max_escY)
                        }
                    ),
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5),
                    iaa.Flipud()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-EscFlipVertRuido.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def escalaFlipVerticalCisalhamento(self, valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY, minCisalhamento, maxCisalhamento):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        scale={
                            "x": (valor_decimal_min_escX, valor_decimal_max_escX),
                            "y": (valor_decimal_min_escY, valor_decimal_max_escY)
                        },
                        shear=(minCisalhamento, maxCisalhamento)
                    ),
                    iaa.Flipud()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-EscFlipVertCis.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def escalaFlipVerticalCorte(self, valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY, relacaoCorte):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        scale={
                            "x": (valor_decimal_min_escX, valor_decimal_max_escX),
                            "y": (valor_decimal_min_escY, valor_decimal_max_escY)
                        },
                    ),
                    iaa.Crop(percent=(0, relacaoCorte)),
                    iaa.Flipud()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-EscFlipVertCorte.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])

    def escalaFlipVerticalCisalhamentoRuidoGaussiano(self, valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY, minCisalhamento, maxCisalhamento, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        scale={
                            "x": (valor_decimal_min_escX, valor_decimal_max_escX),
                            "y": (valor_decimal_min_escY, valor_decimal_max_escY)
                        },
                        shear=(minCisalhamento, maxCisalhamento)
                    ),
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5),
                    iaa.Flipud()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-EscFlipVertCisruido.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def escalaFlipVerticalCorteRuidoGaussiano(self, valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY, relacaoCorte, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        scale={
                            "x": (valor_decimal_min_escX, valor_decimal_max_escX),
                            "y": (valor_decimal_min_escY, valor_decimal_max_escY)
                        },
                    ),
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5),
                    iaa.Crop(percent=(0, relacaoCorte)),
                    iaa.Flipud()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-EscFlipvertCorteRuido.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def escalaFlipHorizontal(self, valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        scale={
                            "x": (valor_decimal_min_escX, valor_decimal_max_escX),
                            "y": (valor_decimal_min_escY, valor_decimal_max_escY)
                        }
                    ),
                    iaa.Fliplr()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-EscFlipHoriz.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def escalaFlipHorizontalRuidoGaussiano(self, valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        scale={
                            "x": (valor_decimal_min_escX, valor_decimal_max_escX),
                            "y": (valor_decimal_min_escY, valor_decimal_max_escY)
                        }
                    ),
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5),
                    iaa.Fliplr()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-EscFlipHorizRuido.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def escalaFlipHorizontalCisalhamento(self, valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY, minCisalhamento, maxCisalhamento):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        scale={
                            "x": (valor_decimal_min_escX, valor_decimal_max_escX),
                            "y": (valor_decimal_min_escY, valor_decimal_max_escY)
                        },
                        shear=(minCisalhamento, maxCisalhamento)
                    ),
                    iaa.Fliplr()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-EscFlipHorizCis.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def escalaFlipHorizontalCorte(self, valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY, relacaoCorte):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        scale={
                            "x": (valor_decimal_min_escX, valor_decimal_max_escX),
                            "y": (valor_decimal_min_escY, valor_decimal_max_escY)
                        },
                    ),
                    iaa.Crop(percent=(0, relacaoCorte)),
                    iaa.Fliplr()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-EscFlipHorizCorte.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def escalaFlipHorizontalCisalhamentoRuidoGaussiano(self, valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY, minCisalhamento, maxCisalhamento, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        scale={
                            "x": (valor_decimal_min_escX, valor_decimal_max_escX),
                            "y": (valor_decimal_min_escY, valor_decimal_max_escY)
                        },
                        shear=(minCisalhamento, maxCisalhamento)
                    ),
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5),
                    iaa.Fliplr()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-EscFlipHorizCisRuido.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def escalaFlipHorizontalCorteRuidoGaussiano(self, valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY, relacaoCorte, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        scale={
                            "x": (valor_decimal_min_escX, valor_decimal_max_escX),
                            "y": (valor_decimal_min_escY, valor_decimal_max_escY)
                        },
                    ),
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5),
                    iaa.Crop(percent=(0, relacaoCorte)),
                    iaa.Fliplr()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-EscFlipHorizCorteRuido.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def escalaFlipHorizontalVertical(self,valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Fliplr(),
                    iaa.Affine(
                        scale={
                            "x": (valor_decimal_min_escX, valor_decimal_max_escX),
                            "y": (valor_decimal_min_escY, valor_decimal_max_escY)
                        }
                    ),
                    iaa.Flipud()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-EscFlipHorizVert.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def escalaFlipHorizontalVerticalRuidoGaussiano(self, valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        scale={
                            "x": (valor_decimal_min_escX, valor_decimal_max_escX),
                            "y": (valor_decimal_min_escY, valor_decimal_max_escY)
                        }
                    ),
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5),
                    iaa.Fliplr(),
                    iaa.Flipud()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-EscFlipHorizVertRuido.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def escalaFlipHorizontalVerticalCisalhamento(self, valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY, minCisalhamento, maxCisalhamento):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        scale={
                            "x": (valor_decimal_min_escX, valor_decimal_max_escX),
                            "y": (valor_decimal_min_escY, valor_decimal_max_escY)
                        }
                        ,
                        shear=(minCisalhamento, maxCisalhamento)
                    ),
                    iaa.Fliplr(),
                    iaa.flipud()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-EscFlipHorizVertCis.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def escalaFlipHorizontalVerticalCorte(self, valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY, relacaoCorte):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        scale={
                            "x": (valor_decimal_min_escX, valor_decimal_max_escX),
                            "y": (valor_decimal_min_escY, valor_decimal_max_escY)
                        }

                    ),
                    iaa.Crop(percent=(0, relacaoCorte)),
                    iaa.Fliplr(),
                    iaa.Flipud()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-EscFlipHorizVertCorte.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def escalaFlipHorizontalVerticalCisalhamentoRuidoGaussiano(self, valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY, minCisalhamento, maxCisalhamento, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        scale={
                            "x": (valor_decimal_min_escX, valor_decimal_max_escX),
                            "y": (valor_decimal_min_escY, valor_decimal_max_escY)
                        },
                        shear=(minCisalhamento, maxCisalhamento)
                    ),
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5),
                    iaa.Flipud(),
                    iaa.Fliplr()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-EscFlipHorizVertCisRuido.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def escalaFlipHorizontalVerticalCorteRuidoGaussiano(self, valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY, relacaoCorte, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        scale={
                            "x": (valor_decimal_min_escX, valor_decimal_max_escX),
                            "y": (valor_decimal_min_escY, valor_decimal_max_escY)
                        }

                    ),
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5),
                    iaa.Crop(percent=(0, relacaoCorte)),
                    iaa.Flipud(),
                    iaa.Fliplr()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-EscFlipHorizVertCorteRuido.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def translacao(self, valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        translate_percent={
                            "x": (valor_decimal_min_transX, valor_decimal_max_transX),
                            "y": (valor_decimal_min_transY, valor_decimal_max_transY)
                        }
                    )
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-Transl.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def translacaoRuidoGaussiano(self, valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        translate_percent={
                            "x": (valor_decimal_min_transX, valor_decimal_max_transX),
                            "y": (valor_decimal_min_transY, valor_decimal_max_transY)
                        }),
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5)
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-TranslRuido.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def translacaoCisalhamento(self, valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY, minCisalhamento, maxCisalhamento):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        translate_percent={
                            "x": (valor_decimal_min_transX, valor_decimal_max_transX),
                            "y": (valor_decimal_min_transY, valor_decimal_max_transY)
                        },
                        shear=(minCisalhamento, maxCisalhamento)
                    )
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-TranslCis.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def translacaoCorte(self, valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY, relacaoCorte):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        translate_percent={
                            "x": (valor_decimal_min_transX, valor_decimal_max_transX),
                            "y": (valor_decimal_min_transY, valor_decimal_max_transY)
                        }
                    ),
                    iaa.Crop(percent=(0, relacaoCorte))
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-TranslCorte.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def translacaoCisalhamentoRuidoGaussiano(self, valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY, minCisalhamento, maxCisalhamento, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        translate_percent={
                            "x": (valor_decimal_min_transX, valor_decimal_max_transX),
                            "y": (valor_decimal_min_transY, valor_decimal_max_transY)
                        },
                        shear=(minCisalhamento, maxCisalhamento)
                    ),
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5)
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-TranslCisRuido.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def translacaoCorteRuidoGaussiano(self, valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY, relacaoCorte, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        translate_percent={
                            "x": (valor_decimal_min_transX, valor_decimal_max_transX),
                            "y": (valor_decimal_min_transY, valor_decimal_max_transY)
                        }
                    ),
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5),
                    iaa.Crop(percent=(0, relacaoCorte))
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-TranslCorteRuido.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def translacaoFlipVertical(self, valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        translate_percent={
                            "x": (valor_decimal_min_transX, valor_decimal_max_transX),
                            "y": (valor_decimal_min_transY, valor_decimal_max_transY)
                        }
                    ),
                    iaa.Flipud()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-TranslFlipVert.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def translacaoFlipVerticalRuidoGaussiano(self, valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        translate_percent={
                            "x": (valor_decimal_min_transX, valor_decimal_max_transX),
                            "y": (valor_decimal_min_transY, valor_decimal_max_transY)
                        }
                    ),
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5),
                    iaa.Flipud()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-TranslFlipVertRuido.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def translacaoFlipVerticalCisalhamento(self, valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY, minCisalhamento, maxCisalhamento):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        translate_percent={
                            "x": (valor_decimal_min_transX, valor_decimal_max_transX),
                            "y": (valor_decimal_min_transY, valor_decimal_max_transY)
                        },
                        shear=(minCisalhamento, maxCisalhamento)
                    ),
                    iaa.Flipud()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-TranslFlipVertCis.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def translacaoFlipVerticalCorte(self, valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY, relacaoCorte):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        translate_percent={
                            "x": (valor_decimal_min_transX, valor_decimal_max_transX),
                            "y": (valor_decimal_min_transY, valor_decimal_max_transY)
                        }
                    ),
                    iaa.Crop(percent=(0, relacaoCorte)),
                    iaa.Flipud()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-TranslFlipVertCorte.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def translacaoFlipVerticalCisalhamentoRuidoGaussiano(self, valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY, minCisalhamento, maxCisalhamento, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        translate_percent={
                            "x": (valor_decimal_min_transX, valor_decimal_max_transX),
                            "y": (valor_decimal_min_transY, valor_decimal_max_transY)
                        },
                        shear=(minCisalhamento, maxCisalhamento)
                    ),
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5),
                    iaa.Flipud()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-TranslFlipVertCisRuido.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def translacaoFlipVerticalCorteRuidoGaussiano(self, valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY, relacaoCorte, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        translate_percent={
                            "x": (valor_decimal_min_transX, valor_decimal_max_transX),
                            "y": (valor_decimal_min_transY, valor_decimal_max_transY)
                        }
                    ),
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5),
                    iaa.Crop(percent=(0, relacaoCorte)),
                    iaa.Flipud()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-TranslFlipVertCorteRuido.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def translacaoFlipHorizontal(self, valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        translate_percent={
                            "x": (valor_decimal_min_transX, valor_decimal_max_transX),
                            "y": (valor_decimal_min_transY, valor_decimal_max_transY)
                        }
                    ),
                    iaa.Fliplr()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-TranslFlipHoriz.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])

    def translacaoFlipHorizontalRuidoGaussiano(self, valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        translate_percent={
                            "x": (valor_decimal_min_transX, valor_decimal_max_transX),
                            "y": (valor_decimal_min_transY, valor_decimal_max_transY)
                        }
                    ),
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5),
                    iaa.Fliplr()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-TranslFlipHorizRuido.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])

    def translacaoFlipHorizontalCisalhamento(self, valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY, minCisalhamento, maxCisalhamento):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        translate_percent={
                            "x": (valor_decimal_min_transX, valor_decimal_max_transX),
                            "y": (valor_decimal_min_transY, valor_decimal_max_transY)
                        },
                        shear=(minCisalhamento, maxCisalhamento)
                    ),
                    iaa.Fliplr()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-TranslFlipHorizCis.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])

    def translacaoFlipHorizontalCorte(self, valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY, relacaoCorte):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        translate_percent={
                            "x": (valor_decimal_min_transX, valor_decimal_max_transX),
                            "y": (valor_decimal_min_transY, valor_decimal_max_transY)
                        },
                    ),
                    iaa.Crop(percent=(0, relacaoCorte)),
                    iaa.Fliplr()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-TranslFlipHorizCorte.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])

    def translacaoFlipHorizontalCisalhamentoRuidoGaussiano(self, valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY, minCisalhamento, maxCisalhamento, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        translate_percent={
                            "x": (valor_decimal_min_transX, valor_decimal_max_transX),
                            "y": (valor_decimal_min_transY, valor_decimal_max_transY)
                        }
                        ,
                        shear=(minCisalhamento, maxCisalhamento)
                    ),
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5),
                    iaa.Fliplr()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-TranslFlipHorizCisRuido.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])

    def translacaoFlipHorizontalCorteRuidoGaussiano(self, valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY, relacaoCorte, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        translate_percent={
                            "x": (valor_decimal_min_transX, valor_decimal_max_transX),
                            "y": (valor_decimal_min_transY, valor_decimal_max_transY)
                        },
                    ),
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5),
                    iaa.Crop(percent=(0, relacaoCorte)),
                    iaa.Fliplr()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-TranslFlipHorizCorteRuido.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])

    def translacaoFlipHorizontalVertical(self,valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Fliplr(),
                    iaa.Affine(
                        translate_percent={
                            "x": (valor_decimal_min_transX, valor_decimal_max_transX),
                            "y": (valor_decimal_min_transY, valor_decimal_max_transY)
                        }
                    ),
                    iaa.Flipud()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-TranslFlipHorizVert.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def translacaoFlipHorizontalVerticalRuidoGaussiano(self, valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        translate_percent={
                            "x": (valor_decimal_min_transX, valor_decimal_max_transX),
                            "y": (valor_decimal_min_transY, valor_decimal_max_transY)
                        }
                    ),
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5),
                    iaa.Fliplr(),
                    iaa.Flipud()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-TranslFlipHorizVertRuido.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def translacaoFlipHorizontalVerticalCisalhamento(self, valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY, minCisalhamento, maxCisalhamento):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        translate_percent={
                            "x": (valor_decimal_min_transX, valor_decimal_max_transX),
                            "y": (valor_decimal_min_transY, valor_decimal_max_transY)
                        }
                        ,
                        shear=(minCisalhamento, maxCisalhamento)
                    ),
                    iaa.Fliplr(),
                    iaa.flipud()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-TranslFlipHorizVertCis.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def translacaoFlipHorizontalVerticalCorte(self, valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY, relacaoCorte):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        translate_percent={
                            "x": (valor_decimal_min_transX, valor_decimal_max_transX),
                            "y": (valor_decimal_min_transY, valor_decimal_max_transY)
                        }

                    ),
                    iaa.Crop(percent=(0, relacaoCorte)),
                    iaa.Fliplr(),
                    iaa.Flipud()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-TranslFlipHorizVertCorte.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def translacaoFlipHorizontalVerticalCisalhamentoRuidoGaussiano(self, valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY, minCisalhamento, maxCisalhamento, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        translate_percent={
                            "x": (valor_decimal_min_transX, valor_decimal_max_transX),
                            "y": (valor_decimal_min_transY, valor_decimal_max_transY)
                        },
                        shear=(minCisalhamento, maxCisalhamento)
                    ),
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5),
                    iaa.Flipud(),
                    iaa.Fliplr()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-TranslFlipHorizVertCisRuido.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])


    def translacaoFlipHorizontalVerticalCorteRuidoGaussiano(self, valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY, relacaoCorte, ruido, desvioPadrao):
        for self.imagem in self.arquivos:
            start = time.time()
            nome_arquivo_imagem = cv2.imread(self.dataset + '/' + self.imagem)
            self.images = np.array(
                [nome_arquivo_imagem for _ in range(self.quantidade)])
            sequencia = iaa.Sequential(
                [
                    iaa.Affine(
                        translate_percent={
                            "x": (valor_decimal_min_transX, valor_decimal_max_transX),
                            "y": (valor_decimal_min_transY, valor_decimal_max_transY)
                        }
                    ),
                    iaa.AdditiveGaussianNoise(
                        loc=ruido, scale=(0.0, desvioPadrao * 255),
                        per_channel=0.5),
                    iaa.Crop(percent=(0, relacaoCorte)),
                    iaa.Flipud(),
                    iaa.Fliplr()
                ],
                random_order=True)
            imagens_aug = sequencia.augment_images(self.images)

            for i in range(self.quantidade):
                arquivo_guardado_na_pasta = (self.pastaSaida + "/" + self.imagem + str(i + 1) + "-TranslFlipHorizVertCorteRuido.png")
                cv2.imwrite(arquivo_guardado_na_pasta, imagens_aug[i])
                end = time.time()
                print (psutil.virtual_memory()[2])
