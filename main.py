from tkinter import filedialog
from tkinter import *
import time
from tkinter import Tk, ttk
from tkinter import messagebox
import tkinter as tk
from Processador_Imagem import Image_Processing

#--------------------
#Cores Utilizadas
cor0 = "#f0f3f5"  # Preta / black
cor1 = "#feffff"  # branca / white
cor2 = "#3fb5a3"  # verde / green
cor3 = "#38576b"  # valor / value
cor4 = "#403d3d"   # letra / letters


def iniciarDataAugmentation():

    dataset = dirEntrada
    pastaSaida = dirSaida
    qtd = int(ent_quantidade.get())
    processar = Image_Processing(dataset, pastaSaida, qtd)


    # Ruído Gaussiano
    if (int(valor_rb_TransGeo.get()) == 0 and int(valor_cb_flipHorizontal.get()) == 0 and int(
            valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 0 and int(
            valor_cb_ruidoGaussiano.get()) == 1):

        valorRuido = valor_ent_ValorRuido.get()
        valorDesvioPadrao = valor_ent_DesvPad.get()
        processar.ruidoGaussiano(valorRuido, valorDesvioPadrao)
        end2 = time.time()

    #Cisalhamento
    if (int(valor_rb_TransGeo.get()) == 0 and int(valor_cb_flipHorizontal.get()) == 0
        and int(valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 1
        and int(valor_cb_ruidoGaussiano.get()) == 0):
        minCisalhamento = int (valor_ent_MinCis.get())
        maxCisalhamento = int (valor_ent_MaxCis.get())
        processar.cisalhamento(minCisalhamento, maxCisalhamento)

    #Corte
    if (int(valor_rb_TransGeo.get()) == 0 and int(valor_cb_flipHorizontal.get()) == 0
    and int(valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 2
    and int(valor_cb_ruidoGaussiano.get()) == 0):
        valorDecimalCorte = int(valor_ent_Corte.get()) / 100
        processar.corte(valorDecimalCorte)

    #Cisalhamento, Ruído Gaussiano
    if (int(valor_rb_TransGeo.get()) == 0 and int(valor_cb_flipHorizontal.get()) == 0
        and int(valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 1
        and int(valor_cb_ruidoGaussiano.get()) == 1):
        minCisalhamento = int(valor_ent_MinCis.get())
        maxCisalhamento = int(valor_ent_MaxCis.get())
        valorRuido = valor_ent_ValorRuido.get()
        valorDesvioPadrao = valor_ent_DesvPad.get()
        processar.cisalhamentoRuidoGaussiano(minCisalhamento, maxCisalhamento, valorRuido, valorDesvioPadrao)

    #Corte, Ruído Gaussiano
    if (int(valor_rb_TransGeo.get()) == 0 and int(valor_cb_flipHorizontal.get()) == 0
        and int(valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 2
        and int(valor_cb_ruidoGaussiano.get()) == 1):
        valorDecimalCorte = int(valor_ent_Corte.get()) / 100
        valorRuido = valor_ent_ValorRuido.get()
        valorDesvioPadrao = valor_ent_DesvPad.get()
        processar.corteRuidoGaussiano(valorDecimalCorte, valorRuido, valorDesvioPadrao)

    #Flip Vertical
    if (int(valor_rb_TransGeo.get()) == 0 and int(valor_cb_flipHorizontal.get()) == 0
        and int(valor_cb_flipVertical.get()) == 1 and int(valor_rb_CorteCis.get()) == 0
        and int(valor_cb_ruidoGaussiano.get()) == 0):
        processar.flipVertical()

    #Flip Vertical, Ruido Gaussiano
    if (int(valor_rb_TransGeo.get()) == 0 and int(valor_cb_flipHorizontal.get()) == 0
        and int(valor_cb_flipVertical.get()) == 1 and int(valor_rb_CorteCis.get()) == 0
        and int(valor_cb_ruidoGaussiano.get()) == 1):
        valorRuido = valor_ent_ValorRuido.get()
        valorDesvioPadrao = valor_ent_DesvPad.get()
        processar.flipVerticalRuidoGaussiano(valorRuido, valorDesvioPadrao)


    #Flip Vertical, Cisalhamento
    if (int(valor_rb_TransGeo.get()) == 0 and int(valor_cb_flipHorizontal.get()) == 0
        and int(valor_cb_flipVertical.get()) == 1 and int(valor_rb_CorteCis.get()) == 1
        and int(valor_cb_ruidoGaussiano.get()) == 0):
        minCisalhamento = int(valor_ent_MinCis.get())
        maxCisalhamento = int(valor_ent_MaxCis.get())
        processar.flipVerticalCisalhamento(minCisalhamento, maxCisalhamento)

    #Flip Vertical, Corte
    if (int(valor_rb_TransGeo.get()) == 0 and int(valor_cb_flipHorizontal.get()) == 0
        and int(valor_cb_flipVertical.get()) == 1 and int(valor_rb_CorteCis.get()) == 2
        and int(valor_cb_ruidoGaussiano.get()) == 0):
        valorDecimalCorte = int(valor_ent_Corte.get()) / 100
        processar.flipVerticalCorte(valorDecimalCorte)

    #Flip Vertical, Cisalhamento, Adição Ruído
    if (int(valor_rb_TransGeo.get()) == 0 and int(valor_cb_flipHorizontal.get()) == 0
        and int(valor_cb_flipVertical.get()) == 1 and int(valor_rb_CorteCis.get()) == 1
        and int(valor_cb_ruidoGaussiano.get()) == 1):
        minCisalhamento = int(valor_ent_MinCis.get())
        maxCisalhamento = int(valor_ent_MaxCis.get())
        valorRuido = valor_ent_ValorRuido.get()
        valorDesvioPadrao = valor_ent_DesvPad.get()
        processar.flipVerticalCisalhamentoRuidoGaussiano(minCisalhamento, maxCisalhamento, valorRuido, valorDesvioPadrao)

    #Flip Vertical, Corte, Adição Ruído
    if (int(valor_rb_TransGeo.get()) == 0 and int(valor_cb_flipHorizontal.get()) == 0
        and int(valor_cb_flipVertical.get()) == 1 and int(valor_rb_CorteCis.get()) == 2
        and int(valor_cb_ruidoGaussiano.get()) == 1):
        valorDecimalCorte = int(valor_ent_Corte.get()) / 100
        valorRuido = valor_ent_ValorRuido.get()
        valorDesvioPadrao = valor_ent_DesvPad.get()
        processar.flipVerticalCorteRuidoGaussiano(valorDecimalCorte, valorRuido, valorDesvioPadrao)

    #Flip Horizontal
    if (int(valor_rb_TransGeo.get()) == 0 and int(valor_cb_flipHorizontal.get()) == 1
        and int(valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 0
        and int(valor_cb_ruidoGaussiano.get()) == 0):
        processar.flipHorizontal()

    #Flip Horizontal, Ruido Gaussiano
    if (int(valor_rb_TransGeo.get()) == 0 and int(valor_cb_flipHorizontal.get()) == 1
        and int(valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 0
        and int(valor_cb_ruidoGaussiano.get()) == 1):
        valorRuido = valor_ent_ValorRuido.get()
        valorDesvioPadrao = valor_ent_DesvPad.get()
        processar.flipHorizontalRuidoGaussiano(valorRuido, valorDesvioPadrao)


    #Flip Horizontal, Cisalhamento
    if (int(valor_rb_TransGeo.get()) == 0 and int(valor_cb_flipHorizontal.get()) == 1
        and int(valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 1
        and int(valor_cb_ruidoGaussiano.get()) == 0):
        minCisalhamento = int(valor_ent_MinCis.get())
        maxCisalhamento = int(valor_ent_MaxCis.get())
        processar.flipHorizontalCisalhamento(minCisalhamento, maxCisalhamento)

    #Flip Horizontal, Corte
    if (int(valor_rb_TransGeo.get()) == 0 and int(valor_cb_flipHorizontal.get()) == 1
        and int(valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 2
        and int(valor_cb_ruidoGaussiano.get()) == 0):
        valorDecimalCorte = int(valor_ent_Corte.get()) / 100
        processar.flipHorizontalCorte(valorDecimalCorte)

    #Flip Horizontal, Cisalhamento, Adição Ruído
    if (int(valor_rb_TransGeo.get()) == 0 and int(valor_cb_flipHorizontal.get()) == 1
        and int(valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 1
        and int(valor_cb_ruidoGaussiano.get()) == 1):
        minCisalhamento = int(valor_ent_MinCis.get())
        maxCisalhamento = int(valor_ent_MaxCis.get())
        valorRuido = valor_ent_ValorRuido.get()
        valorDesvioPadrao = valor_ent_DesvPad.get()
        processar.flipHorizontalCisalhamentoRuidoGaussiano(minCisalhamento, maxCisalhamento, valorRuido, valorDesvioPadrao)

    #Flip Horizontal, Corte, Adição Ruído
    if (int(valor_rb_TransGeo.get()) == 0 and int(valor_cb_flipHorizontal.get()) == 1
        and int(valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 2
        and int(valor_cb_ruidoGaussiano.get()) == 1):
        valorDecimalCorte = int(valor_ent_Corte.get()) / 100
        valorRuido = valor_ent_ValorRuido.get()
        valorDesvioPadrao = valor_ent_DesvPad.get()
        processar.flipHorizontalCorteRuidoGaussiano(valorDecimalCorte, valorRuido, valorDesvioPadrao)

    #Flip Horizontal e Flip Vertical
    if (int(valor_rb_TransGeo.get()) == 0 and int(valor_cb_flipHorizontal.get()) == 1
        and int(valor_cb_flipVertical.get()) == 1 and int(valor_rb_CorteCis.get()) == 0
        and int(valor_cb_ruidoGaussiano.get()) == 0):
        processar.flipHorizontalVertical()

    #Flip Horizontal, Flip Vertical, Ruido Gaussiano
    if (int(valor_rb_TransGeo.get()) == 0 and int(valor_cb_flipHorizontal.get()) == 1
        and int(valor_cb_flipVertical.get()) == 1 and int(valor_rb_CorteCis.get()) == 0
        and int(valor_cb_ruidoGaussiano.get()) == 1):
        valorRuido = valor_ent_ValorRuido.get()
        valorDesvioPadrao = valor_ent_DesvPad.get()
        processar.flipHorizontalRuidoGaussiano(valorRuido, valorDesvioPadrao)


    #Flip Horizontal, Flip Vertical, Cisalhamento
    if (int(valor_rb_TransGeo.get()) == 0 and int(valor_cb_flipHorizontal.get()) == 1
        and int(valor_cb_flipVertical.get()) == 1 and int(valor_rb_CorteCis.get()) == 1
        and int(valor_cb_ruidoGaussiano.get()) == 0):
        minCisalhamento = int(valor_ent_MinCis.get())
        maxCisalhamento = int(valor_ent_MaxCis.get())
        processar.flipHorizontalCisalhamento(minCisalhamento, maxCisalhamento)

    #Flip Horizontal, Flip Vertical, Corte
    if (int(valor_rb_TransGeo.get()) == 0 and int(valor_cb_flipHorizontal.get()) == 1
        and int(valor_cb_flipVertical.get()) == 1 and int(valor_rb_CorteCis.get()) == 2
        and int(valor_cb_ruidoGaussiano.get()) == 0):
        valorDecimalCorte = int(valor_ent_Corte.get()) / 100
        processar.flipHorizontalVerticalCorte(valorDecimalCorte)

    #Flip Horizontal, Flip Vertical, Cisalhamento, Adição Ruído
    if (int(valor_rb_TransGeo.get()) == 0 and int(valor_cb_flipHorizontal.get()) == 1
        and int(valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 1
        and int(valor_cb_ruidoGaussiano.get()) == 1):
        minCisalhamento = int(valor_ent_MinCis.get())
        maxCisalhamento = int(valor_ent_MaxCis.get())
        valorRuido = valor_ent_ValorRuido.get()
        valorDesvioPadrao = valor_ent_DesvPad.get()
        processar.flipHorizontalVerticalCisalhamentoRuidoGaussiano(minCisalhamento, maxCisalhamento, valorRuido, valorDesvioPadrao)

    #Flip Horizontal, Flip Vertical, Corte, Adição Ruído
    if (int(valor_rb_TransGeo.get()) == 0 and int(valor_cb_flipHorizontal.get()) == 1
        and int(valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 2
        and int(valor_cb_ruidoGaussiano.get()) == 1):
        valorDecimalCorte = int(valor_ent_Corte.get()) / 100
        valorRuido = valor_ent_ValorRuido.get()
        valorDesvioPadrao = valor_ent_DesvPad.get()
        processar.flipHorizontalVerticalCorteRuidoGaussiano(valorDecimalCorte, valorRuido, valorDesvioPadrao)

    #Rotação
    if (int(valor_rb_TransGeo.get()) == 1 and int(valor_cb_flipHorizontal.get()) == 0 and int(valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 0 and int(valor_cb_ruidoGaussiano.get()) == 0):
        MinRot = valor_ent_MinRot.get()
        MaxRot = valor_ent_MaxRot.get()
        processar.rotacao(MinRot, MaxRot)

    #Rotação, Ruido Gaussiano
    if (int(valor_rb_TransGeo.get()) == 1 and int(valor_cb_flipHorizontal.get()) == 0 and int(valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 0 and int(valor_cb_ruidoGaussiano.get()) == 1):
        MinRot = valor_ent_MinRot.get()
        MaxRot = valor_ent_MaxRot.get()
        valorRuido = valor_ent_ValorRuido.get()
        valorDesvioPadrao = valor_ent_DesvPad.get()
        processar.rotacaoRuidoGaussiano(MinRot, MaxRot, valorRuido, valorDesvioPadrao)

    #Rotação,Cisalhamento
    if (int(valor_rb_TransGeo.get()) == 1 and int(valor_cb_flipHorizontal.get()) == 0 and int(valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 1 and int(valor_cb_ruidoGaussiano.get()) == 0):
        MinRot = valor_ent_MinRot.get()
        MaxRot = valor_ent_MaxRot.get()
        minCisalhamento = int(valor_ent_MinCis.get())
        maxCisalhamento = int(valor_ent_MaxCis.get())
        processar.rotacaoCisalhamento(MinRot, MaxRot, minCisalhamento, maxCisalhamento)

    #Rotação,Corte
    if (int(valor_rb_TransGeo.get()) == 1 and int(valor_cb_flipHorizontal.get()) == 0 and int(valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 2 and int(valor_cb_ruidoGaussiano.get()) == 0):
        MinRot = valor_ent_MinRot.get()
        MaxRot = valor_ent_MaxRot.get()
        valorDecimalCorte = int(valor_ent_Corte.get()) / 100
        processar.rotacaoCorte(MinRot, MaxRot, valorDecimalCorte)

    #Rotação, Cisalhamento, Ruido Gaussiano
    if (int(valor_rb_TransGeo.get()) == 1 and int(valor_cb_flipHorizontal.get()) == 0 and int(valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 1 and int(valor_cb_ruidoGaussiano.get()) == 1):
        MinRot = valor_ent_MinRot.get()
        MaxRot = valor_ent_MaxRot.get()
        minCisalhamento = int(valor_ent_MinCis.get())
        maxCisalhamento = int(valor_ent_MaxCis.get())
        valorRuido = valor_ent_ValorRuido.get()
        valorDesvioPadrao = valor_ent_DesvPad.get()
        processar.rotacaoCisalhamentoRuidoGaussiano(MinRot, MaxRot, minCisalhamento, maxCisalhamento, valorRuido, valorDesvioPadrao)

    #Rotação, Corte, Ruido Gaussiano
    if (int(valor_rb_TransGeo.get()) == 1 and int(valor_cb_flipHorizontal.get()) == 0 and int(valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 2 and int(valor_cb_ruidoGaussiano.get()) == 1):
        MinRot = valor_ent_MinRot.get()
        MaxRot = valor_ent_MaxRot.get()
        valorDecimalCorte = int(valor_ent_Corte.get()) / 100
        valorRuido = valor_ent_ValorRuido.get()
        valorDesvioPadrao = valor_ent_DesvPad.get()
        processar.rotacaoCorteRuidoGaussiano(MinRot, MaxRot, valorDecimalCorte, valorRuido, valorDesvioPadrao)

    #Rotação, Flip Vertical
    if (int(valor_rb_TransGeo.get()) == 1 and int(valor_cb_flipHorizontal.get()) == 0
        and int(valor_cb_flipVertical.get()) == 1 and int(valor_rb_CorteCis.get()) == 0
        and int(valor_cb_ruidoGaussiano.get()) == 0):
        MinRot = valor_ent_MinRot.get()
        MaxRot = valor_ent_MaxRot.get()
        processar.rotacaoFlipVertical(MinRot, MaxRot)

    #Rotação, Flip Vertical, Ruído Gaussiano
    if (int(valor_rb_TransGeo.get()) == 1 and int(valor_cb_flipHorizontal.get()) == 0
        and int(valor_cb_flipVertical.get()) == 1 and int(valor_rb_CorteCis.get()) == 0
        and int(valor_cb_ruidoGaussiano.get()) == 1):
        MinRot = valor_ent_MinRot.get()
        MaxRot = valor_ent_MaxRot.get()
        valorRuido = valor_ent_ValorRuido.get()
        valorDesvioPadrao = valor_ent_DesvPad.get()
        processar.rotacaoFlipVerticalRuidoGaussiano(MinRot, MaxRot, valorRuido,valorDesvioPadrao)

    #Rotação, FLip Vertical, Cisalhamento
    if (int(valor_rb_TransGeo.get()) == 1 and int(valor_cb_flipHorizontal.get()) == 0
            and int(valor_cb_flipVertical.get()) == 1 and int(valor_rb_CorteCis.get()) == 1 and int(valor_cb_ruidoGaussiano.get()) == 0):
        MinRot = valor_ent_MinRot.get()
        MaxRot = valor_ent_MaxRot.get()
        minCisalhamento = int(valor_ent_MinCis.get())
        maxCisalhamento = int(valor_ent_MaxCis.get())
        processar.rotacaoFlipVerticalCisalhamento(MinRot, MaxRot, minCisalhamento, maxCisalhamento)

    #Rotação, Flip Vertical, Corte
    if (int(valor_rb_TransGeo.get()) == 1 and int(valor_cb_flipHorizontal.get()) == 0 and int(valor_cb_flipVertical.get()) == 1 and int(valor_rb_CorteCis.get()) == 2 and int(valor_cb_ruidoGaussiano.get()) == 0):
        MinRot = valor_ent_MinRot.get()
        MaxRot = valor_ent_MaxRot.get()
        valorDecimalCorte = int(valor_ent_Corte.get()) / 100
        processar.rotacaoFlipVerticalCorte(MinRot, MaxRot, valorDecimalCorte)

    #Rotação, Flip Vertical, Cisalhamento, Ruído Gaussiano
    if (int(valor_rb_TransGeo.get()) == 1 and int(valor_cb_flipHorizontal.get()) == 0 and int(valor_cb_flipVertical.get()) == 1 and int(valor_rb_CorteCis.get()) == 1 and int(valor_cb_ruidoGaussiano.get()) == 1):
        MinRot = valor_ent_MinRot.get()
        MaxRot = valor_ent_MaxRot.get()
        minCisalhamento = int(valor_ent_MinCis.get())
        maxCisalhamento = int(valor_ent_MaxCis.get())
        valorRuido = valor_ent_ValorRuido.get()
        valorDesvioPadrao = valor_ent_DesvPad.get()
        processar.rotacaoFlipVerticalCisalhamentoRuidoGaussiano(MinRot, MaxRot, minCisalhamento, maxCisalhamento, valorRuido, valorDesvioPadrao)

    #Rotação, Flip Vertical, Corte, Ruido Gaussiano
    if (int(valor_rb_TransGeo.get()) == 1 and int(valor_cb_flipHorizontal.get()) == 0 and int(valor_cb_flipVertical.get()) == 1 and int(valor_rb_CorteCis.get()) == 2 and int(valor_cb_ruidoGaussiano.get()) == 1):
        MinRot = valor_ent_MinRot.get()
        MaxRot = valor_ent_MaxRot.get()
        valorDecimalCorte = int(valor_ent_Corte.get()) / 100
        valorRuido = valor_ent_ValorRuido.get()
        valorDesvioPadrao = valor_ent_DesvPad.get()
        processar.rotacaoFlipVerticalCorteRuidoGaussiano(MinRot, MaxRot, valorDecimalCorte, valorRuido, valorDesvioPadrao)

    #Rotação, Flip Horizontal
    if (int(valor_rb_TransGeo.get()) == 1 and int(valor_cb_flipHorizontal.get()) == 1
        and int(valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 0
        and int(valor_cb_ruidoGaussiano.get()) == 0):
        MinRot = valor_ent_MinRot.get()
        MaxRot = valor_ent_MaxRot.get()
        processar.rotacaoFlipHorizontal(MinRot, MaxRot)

    #Rotação, Flip Horizontal, Ruído Gaussiano
    if (int(valor_rb_TransGeo.get()) == 1 and int(valor_cb_flipHorizontal.get()) == 1
        and int(valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 0
        and int(valor_cb_ruidoGaussiano.get()) == 1):
        MinRot = valor_ent_MinRot.get()
        MaxRot = valor_ent_MaxRot.get()
        valorRuido = valor_ent_ValorRuido.get()
        valorDesvioPadrao = valor_ent_DesvPad.get()
        processar.rotacaoFlipHorizontalRuidoGaussiano(MinRot, MaxRot, valorRuido,valorDesvioPadrao)

    #Rotação, FLip Horizontal, Cisalhamento
    if (int(valor_rb_TransGeo.get()) == 1 and int(valor_cb_flipHorizontal.get()) == 1 and int(valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 1 and int(valor_cb_ruidoGaussiano.get()) == 0):
        MinRot = valor_ent_MinRot.get()
        MaxRot = valor_ent_MaxRot.get()
        minCisalhamento = int(valor_ent_MinCis.get())
        maxCisalhamento = int(valor_ent_MaxCis.get())
        processar.rotacaoFlipHorizontalCisalhamento(MinRot, MaxRot, minCisalhamento, maxCisalhamento)

    #Rotação, Flip Horizontal, Corte
    if (int(valor_rb_TransGeo.get()) == 1 and int(valor_cb_flipHorizontal.get()) == 1 and int(valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 2 and int(valor_cb_ruidoGaussiano.get()) == 0):
        MinRot = valor_ent_MinRot.get()
        MaxRot = valor_ent_MaxRot.get()
        valorDecimalCorte = int(valor_ent_Corte.get()) / 100
        processar.rotacaoFlipHorizontalCorte(MinRot, MaxRot, valorDecimalCorte)

    #Rotação, Flip Horizontal, Cisalhamento, Ruído Gaussiano
    if (int(valor_rb_TransGeo.get()) == 1 and int(valor_cb_flipHorizontal.get()) == 1 and int(valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 1 and int(valor_cb_ruidoGaussiano.get()) == 1):
        MinRot = valor_ent_MinRot.get()
        MaxRot = valor_ent_MaxRot.get()
        minCisalhamento = int(valor_ent_MinCis.get())
        maxCisalhamento = int(valor_ent_MaxCis.get())
        valorRuido = valor_ent_ValorRuido.get()
        valorDesvioPadrao = valor_ent_DesvPad.get()
        processar.rotacaoFlipHorizontalCisalhamentoRuidoGaussiano(MinRot, MaxRot, minCisalhamento, maxCisalhamento, valorRuido, valorDesvioPadrao)

    # Rotação, Flip Horizontal, Corte, Adição de Ruido
    if (int(valor_rb_TransGeo.get()) == 1 and int(valor_cb_flipHorizontal.get()) == 1 and int(
         valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 2 and int(
         valor_cb_ruidoGaussiano.get()) == 1):
         MinRot = valor_ent_MinRot.get()
         MaxRot = valor_ent_MaxRot.get()
         valorDecimalCorte = int(valor_ent_Corte.get()) / 100
         valorRuido = valor_ent_ValorRuido.get()
         valorDesvioPadrao = valor_ent_DesvPad.get()
         processar.rotacaoFlipHorizontalCorteRuidoGaussiano(MinRot, MaxRot, valorDecimalCorte, valorRuido, valorDesvioPadrao)

#Rotação, Flip Horizontal, Flip Vertical
    if (int(valor_rb_TransGeo.get()) == 1 and int(valor_cb_flipHorizontal.get()) == 1
        and int(valor_cb_flipVertical.get()) == 1 and int(valor_rb_CorteCis.get()) == 0
        and int(valor_cb_ruidoGaussiano.get()) == 0):
        MinRot = valor_ent_MinRot.get()
        MaxRot = valor_ent_MaxRot.get()
        processar.rotacaoFlipHorizontalVertical(MinRot, MaxRot)

    #Rotação, Flip Horizontal, Flip Vertical, Ruído Gaussiano
    if (int(valor_rb_TransGeo.get()) == 1 and int(valor_cb_flipHorizontal.get()) == 1
        and int(valor_cb_flipVertical.get()) == 1 and int(valor_rb_CorteCis.get()) == 0
        and int(valor_cb_ruidoGaussiano.get()) == 1):
        MinRot = valor_ent_MinRot.get()
        MaxRot = valor_ent_MaxRot.get()
        valorRuido = valor_ent_ValorRuido.get()
        valorDesvioPadrao = valor_ent_DesvPad.get()
        processar.rotacaoFlipHorizontalVerticalRuidoGaussiano(MinRot, MaxRot, valorRuido,valorDesvioPadrao)

    #Rotação, FLip Horizontal, Flip Vertical, Cisalhamento
    if (int(valor_rb_TransGeo.get()) == 1 and int(valor_cb_flipHorizontal.get()) == 1
            and int(valor_cb_flipVertical.get()) == 1 and int(valor_rb_CorteCis.get()) == 1 and int(valor_cb_ruidoGaussiano.get()) == 0):
        MinRot = valor_ent_MinRot.get()
        MaxRot = valor_ent_MaxRot.get()
        minCisalhamento = int(valor_ent_MinCis.get())
        maxCisalhamento = int(valor_ent_MaxCis.get())
        processar.rotacaoFlipHorizontalVerticalCisalhamento(MinRot, MaxRot, minCisalhamento, maxCisalhamento)

    #Rotação, Flip Horizontal, Flip Vertical, Corte
    if (int(valor_rb_TransGeo.get()) == 1 and int(valor_cb_flipHorizontal.get()) == 1
            and int(valor_cb_flipVertical.get()) == 1 and int(valor_rb_CorteCis.get()) == 2 and int(valor_cb_ruidoGaussiano.get()) == 0):
        MinRot = valor_ent_MinRot.get()
        MaxRot = valor_ent_MaxRot.get()
        valorDecimalCorte = int(valor_ent_Corte.get()) / 100
        processar.rotacaoFlipHorizontalVerticalCorte(MinRot, MaxRot, valorDecimalCorte)

    #Rotação, Flip Horizontal, Flip Vertical, Cisalhamento, Ruído Gaussiano
    if (int(valor_rb_TransGeo.get()) == 1 and int(valor_cb_flipHorizontal.get()) == 1
            and int(valor_cb_flipVertical.get()) == 1 and int(valor_rb_CorteCis.get()) == 1
            and int(valor_cb_ruidoGaussiano.get()) == 1):
        MinRot = valor_ent_MinRot.get()
        MaxRot = valor_ent_MaxRot.get()
        minCisalhamento = int(valor_ent_MinCis.get())
        maxCisalhamento = int(valor_ent_MaxCis.get())
        valorRuido = valor_ent_ValorRuido.get()
        valorDesvioPadrao = valor_ent_DesvPad.get()
        processar.rotacaoFlipHorizontalVerticalCisalhamentoRuidoGaussiano(MinRot, MaxRot, minCisalhamento, maxCisalhamento, valorRuido, valorDesvioPadrao)

    #Rotação, Flip Horizontal, Flip Vertical, Corte, Adição de Ruido
    if (int(valor_rb_TransGeo.get()) == 1 and int(valor_cb_flipHorizontal.get()) == 1 and int(
         valor_cb_flipVertical.get()) == 1 and int(valor_rb_CorteCis.get()) == 2 and int(
         valor_cb_ruidoGaussiano.get()) == 1):
         MinRot = valor_ent_MinRot.get()
         MaxRot = valor_ent_MaxRot.get()
         valorDecimalCorte = int(valor_ent_Corte.get()) / 100
         valorRuido = valor_ent_ValorRuido.get()
         valorDesvioPadrao = valor_ent_DesvPad.get()
         processar.rotacaoFlipHorizontalVerticalCorteRuidoGaussiano(MinRot, MaxRot, valorDecimalCorte, valorRuido, valorDesvioPadrao)

    #Escala
    if (int(valor_rb_TransGeo.get()) == 2 and int(valor_cb_flipHorizontal.get()) == 0 and int(valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 0 and int(valor_cb_ruidoGaussiano.get()) == 0):
        valor_decimal_min_escX = valor_ent_MinEscX.get()/100
        valor_decimal_max_escX = valor_ent_MaxEscX.get()/100
        valor_decimal_min_escY = valor_ent_MinEscY.get()/100
        valor_decimal_max_escY = valor_ent_MaxEscY.get()/100
        processar.escala(valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY)

    #Escala, Ruido Gaussiano
    if (int(valor_rb_TransGeo.get()) == 2 and int(valor_cb_flipHorizontal.get()) == 0 and int(valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 0 and int(valor_cb_ruidoGaussiano.get()) == 1):
        valor_decimal_min_escX = valor_ent_MinEscX.get()/100
        valor_decimal_max_escX = valor_ent_MaxEscX.get()/100
        valor_decimal_min_escY = valor_ent_MinEscY.get()/100
        valor_decimal_max_escY = valor_ent_MaxEscY.get()/100
        valorRuido = valor_ent_ValorRuido.get()
        valorDesvioPadrao = valor_ent_DesvPad.get()
        processar.escalaRuidoGaussiano(valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY, valorRuido, valorDesvioPadrao)

    #Escala,Cisalhamento
    if (int(valor_rb_TransGeo.get()) == 2 and int(valor_cb_flipHorizontal.get()) == 0 and int(valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 1 and int(valor_cb_ruidoGaussiano.get()) == 0):
        valor_decimal_min_escX = valor_ent_MinEscX.get()/100
        valor_decimal_max_escX = valor_ent_MaxEscX.get()/100
        valor_decimal_min_escY = valor_ent_MinEscY.get()/100
        valor_decimal_max_escY = valor_ent_MaxEscY.get()/100
        minCisalhamento = int(valor_ent_MinCis.get())
        maxCisalhamento = int(valor_ent_MaxCis.get())
        processar.escalaCisalhamento(valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY, minCisalhamento, maxCisalhamento)

    #Escala,Corte
    if (int(valor_rb_TransGeo.get()) == 2 and int(valor_cb_flipHorizontal.get()) == 0 and int(valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 2 and int(valor_cb_ruidoGaussiano.get()) == 0):
        valor_decimal_min_escX = valor_ent_MinEscX.get()/100
        valor_decimal_max_escX = valor_ent_MaxEscX.get()/100
        valor_decimal_min_escY = valor_ent_MinEscY.get()/100
        valor_decimal_max_escY = valor_ent_MaxEscY.get()/100
        valorDecimalCorte = int(valor_ent_Corte.get()) / 100
        processar.escalaCorte(valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY, valorDecimalCorte)

    #Escala, Cisalhamento, Ruido Gaussiano
    if (int(valor_rb_TransGeo.get()) == 2 and int(valor_cb_flipHorizontal.get()) == 0 and int(valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 1 and int(valor_cb_ruidoGaussiano.get()) == 1):
        valor_decimal_min_escX = valor_ent_MinEscX.get()/100
        valor_decimal_max_escX = valor_ent_MaxEscX.get()/100
        valor_decimal_min_escY = valor_ent_MinEscY.get()/100
        valor_decimal_max_escY = valor_ent_MaxEscY.get()/100
        minCisalhamento = int(valor_ent_MinCis.get())
        maxCisalhamento = int(valor_ent_MaxCis.get())
        valorRuido = valor_ent_ValorRuido.get()
        valorDesvioPadrao = valor_ent_DesvPad.get()
        processar.escalaCisalhamentoRuidoGaussiano(valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY, minCisalhamento, maxCisalhamento, valorRuido, valorDesvioPadrao)

    #Escala, Corte, Ruido Gaussiano
    if (int(valor_rb_TransGeo.get()) == 2 and int(valor_cb_flipHorizontal.get()) == 0 and int(valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 2 and int(valor_cb_ruidoGaussiano.get()) == 1):
        valor_decimal_min_escX = valor_ent_MinEscX.get()/100
        valor_decimal_max_escX = valor_ent_MaxEscX.get()/100
        valor_decimal_min_escY = valor_ent_MinEscY.get()/100
        valor_decimal_max_escY = valor_ent_MaxEscY.get()/100
        valorDecimalCorte = int(valor_ent_Corte.get()) / 100
        valorRuido = valor_ent_ValorRuido.get()
        valorDesvioPadrao = valor_ent_DesvPad.get()
        processar.escalaCorteRuidoGaussiano(valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY, valorDecimalCorte, valorRuido, valorDesvioPadrao)

    #Escala, Flip Vertical
    if (int(valor_rb_TransGeo.get()) == 2 and int(valor_cb_flipHorizontal.get()) == 0
        and int(valor_cb_flipVertical.get()) == 1 and int(valor_rb_CorteCis.get()) == 0
        and int(valor_cb_ruidoGaussiano.get()) == 0):
        valor_decimal_min_escX = valor_ent_MinEscX.get()/100
        valor_decimal_max_escX = valor_ent_MaxEscX.get()/100
        valor_decimal_min_escY = valor_ent_MinEscY.get()/100
        valor_decimal_max_escY = valor_ent_MaxEscY.get()/100
        processar.escalaFlipVertical(valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY)

    #Escala, Flip Vertical, Ruído Gaussiano
    if (int(valor_rb_TransGeo.get()) == 2 and int(valor_cb_flipHorizontal.get()) == 0
        and int(valor_cb_flipVertical.get()) == 1 and int(valor_rb_CorteCis.get()) == 0
        and int(valor_cb_ruidoGaussiano.get()) == 1):
        valor_decimal_min_escX = valor_ent_MinEscX.get()/100
        valor_decimal_max_escX = valor_ent_MaxEscX.get()/100
        valor_decimal_min_escY = valor_ent_MinEscY.get()/100
        valor_decimal_max_escY = valor_ent_MaxEscY.get()/100
        valorRuido = valor_ent_ValorRuido.get()
        valorDesvioPadrao = valor_ent_DesvPad.get()
        processar.escalaFlipVerticalRuidoGaussiano(valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY, valorRuido,valorDesvioPadrao)

    #Escala, FLip Vertical, Cisalhamento
    if (int(valor_rb_TransGeo.get()) == 2 and int(valor_cb_flipHorizontal.get()) == 0
            and int(valor_cb_flipVertical.get()) == 1 and int(valor_rb_CorteCis.get()) == 1 and int(valor_cb_ruidoGaussiano.get()) == 0):
        valor_decimal_min_escX = valor_ent_MinEscX.get()/100
        valor_decimal_max_escX = valor_ent_MaxEscX.get()/100
        valor_decimal_min_escY = valor_ent_MinEscY.get()/100
        valor_decimal_max_escY = valor_ent_MaxEscY.get()/100
        minCisalhamento = int(valor_ent_MinCis.get())
        maxCisalhamento = int(valor_ent_MaxCis.get())
        processar.escalaFlipVerticalCisalhamento(valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY, minCisalhamento, maxCisalhamento)

    #Escala, Flip Vertical, Corte
    if (int(valor_rb_TransGeo.get()) == 2 and int(valor_cb_flipHorizontal.get()) == 0 and int(valor_cb_flipVertical.get()) == 1 and int(valor_rb_CorteCis.get()) == 2 and int(valor_cb_ruidoGaussiano.get()) == 0):
        valor_decimal_min_escX = valor_ent_MinEscX.get()/100
        valor_decimal_max_escX = valor_ent_MaxEscX.get()/100
        valor_decimal_min_escY = valor_ent_MinEscY.get()/100
        valor_decimal_max_escY = valor_ent_MaxEscY.get()/100
        valorDecimalCorte = int(valor_ent_Corte.get()) / 100
        processar.escalaFlipVerticalCorte(valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY, valorDecimalCorte)

    #Escala, Flip Vertical, Cisalhamento, Ruído Gaussiano
    if (int(valor_rb_TransGeo.get()) == 2 and int(valor_cb_flipHorizontal.get()) == 0 and int(valor_cb_flipVertical.get()) == 1 and int(valor_rb_CorteCis.get()) == 1 and int(valor_cb_ruidoGaussiano.get()) == 1):
        valor_decimal_min_escX = valor_ent_MinEscX.get()/100
        valor_decimal_max_escX = valor_ent_MaxEscX.get()/100
        valor_decimal_min_escY = valor_ent_MinEscY.get()/100
        valor_decimal_max_escY = valor_ent_MaxEscY.get()/100
        minCisalhamento = int(valor_ent_MinCis.get())
        maxCisalhamento = int(valor_ent_MaxCis.get())
        valorRuido = valor_ent_ValorRuido.get()
        valorDesvioPadrao = valor_ent_DesvPad.get()
        processar.escalaFlipVerticalCisalhamentoRuidoGaussiano(valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY, minCisalhamento, maxCisalhamento, valorRuido, valorDesvioPadrao)

    #Escala, Flip Vertical, Corte, Ruido Gaussiano
    if (int(valor_rb_TransGeo.get()) == 2 and int(valor_cb_flipHorizontal.get()) == 0 and int(valor_cb_flipVertical.get()) == 1 and int(valor_rb_CorteCis.get()) == 2 and int(valor_cb_ruidoGaussiano.get()) == 1):
        valor_decimal_min_escX = valor_ent_MinEscX.get()/100
        valor_decimal_max_escX = valor_ent_MaxEscX.get()/100
        valor_decimal_min_escY = valor_ent_MinEscY.get()/100
        valor_decimal_max_escY = valor_ent_MaxEscY.get()/100
        valorDecimalCorte = int(valor_ent_Corte.get()) / 100
        valorRuido = valor_ent_ValorRuido.get()
        valorDesvioPadrao = valor_ent_DesvPad.get()
        processar.escalaFlipVerticalCorteRuidoGaussiano(valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY, valorDecimalCorte, valorRuido, valorDesvioPadrao)

    #Escala, Flip Horizontal
    if (int(valor_rb_TransGeo.get()) == 2 and int(valor_cb_flipHorizontal.get()) == 1
        and int(valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 0
        and int(valor_cb_ruidoGaussiano.get()) == 0):
        valor_decimal_min_escX = valor_ent_MinEscX.get()/100
        valor_decimal_max_escX = valor_ent_MaxEscX.get()/100
        valor_decimal_min_escY = valor_ent_MinEscY.get()/100
        valor_decimal_max_escY = valor_ent_MaxEscY.get()/100
        processar.escalaFlipHorizontal(valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY)

    #Escala, Flip Horizontal, Ruído Gaussiano
    if (int(valor_rb_TransGeo.get()) == 2 and int(valor_cb_flipHorizontal.get()) == 1
        and int(valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 0
        and int(valor_cb_ruidoGaussiano.get()) == 1):
        valor_decimal_min_escX = valor_ent_MinEscX.get()/100
        valor_decimal_max_escX = valor_ent_MaxEscX.get()/100
        valor_decimal_min_escY = valor_ent_MinEscY.get()/100
        valor_decimal_max_escY = valor_ent_MaxEscY.get()/100
        valorRuido = valor_ent_ValorRuido.get()
        valorDesvioPadrao = valor_ent_DesvPad.get()
        processar.escalaFlipHorizontalRuidoGaussiano(valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY, valorRuido,valorDesvioPadrao)

    #Escala, FLip Horizontal, Cisalhamento
    if (int(valor_rb_TransGeo.get()) == 2 and int(valor_cb_flipHorizontal.get()) == 1 and int(valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 1 and int(valor_cb_ruidoGaussiano.get()) == 0):
        valor_decimal_min_escX = valor_ent_MinEscX.get()/100
        valor_decimal_max_escX = valor_ent_MaxEscX.get()/100
        valor_decimal_min_escY = valor_ent_MinEscY.get()/100
        valor_decimal_max_escY = valor_ent_MaxEscY.get()/100
        minCisalhamento = int(valor_ent_MinCis.get())
        maxCisalhamento = int(valor_ent_MaxCis.get())
        processar.escalaFlipHorizontalCisalhamento(valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY, minCisalhamento, maxCisalhamento)

    #Escala, Flip Horizontal, Corte
    if (int(valor_rb_TransGeo.get()) == 2 and int(valor_cb_flipHorizontal.get()) == 1 and int(valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 2 and int(valor_cb_ruidoGaussiano.get()) == 0):
        valor_decimal_min_escX = valor_ent_MinEscX.get()/100
        valor_decimal_max_escX = valor_ent_MaxEscX.get()/100
        valor_decimal_min_escY = valor_ent_MinEscY.get()/100
        valor_decimal_max_escY = valor_ent_MaxEscY.get()/100
        valorDecimalCorte = int(valor_ent_Corte.get()) / 100
        processar.escalaFlipHorizontalCorte(valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY, valorDecimalCorte)

    #Escala, Flip Horizontal, Cisalhamento, Ruído Gaussiano
    if (int(valor_rb_TransGeo.get()) == 2 and int(valor_cb_flipHorizontal.get()) == 1 and int(valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 1 and int(valor_cb_ruidoGaussiano.get()) == 1):
        valor_decimal_min_escX = valor_ent_MinEscX.get()/100
        valor_decimal_max_escX = valor_ent_MaxEscX.get()/100
        valor_decimal_min_escY = valor_ent_MinEscY.get()/100
        valor_decimal_max_escY = valor_ent_MaxEscY.get()/100
        minCisalhamento = int(valor_ent_MinCis.get())
        maxCisalhamento = int(valor_ent_MaxCis.get())
        valorRuido = valor_ent_ValorRuido.get()
        valorDesvioPadrao = valor_ent_DesvPad.get()
        processar.escalaFlipHorizontalCisalhamentoRuidoGaussiano(valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY, minCisalhamento, maxCisalhamento, valorRuido, valorDesvioPadrao)

    # Escala, Flip Horizontal, Corte, Adição de Ruido
    if (int(valor_rb_TransGeo.get()) == 2 and int(valor_cb_flipHorizontal.get()) == 1 and int(
         valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 2 and int(
         valor_cb_ruidoGaussiano.get()) == 1):
         valor_decimal_min_escX = valor_ent_MinEscX.get()/100
         valor_decimal_max_escX = valor_ent_MaxEscX.get()/100
         valor_decimal_min_escY = valor_ent_MinEscY.get()/100
         valor_decimal_max_escY = valor_ent_MaxEscY.get()/100
         valorDecimalCorte = int(valor_ent_Corte.get()) / 100
         valorRuido = valor_ent_ValorRuido.get()
         valorDesvioPadrao = valor_ent_DesvPad.get()
         processar.escalaFlipHorizontalCorteRuidoGaussiano(valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY, valorDecimalCorte, valorRuido, valorDesvioPadrao)

#Escala, Flip Horizontal, Flip Vertical
    if (int(valor_rb_TransGeo.get()) == 2 and int(valor_cb_flipHorizontal.get()) == 1
        and int(valor_cb_flipVertical.get()) == 1 and int(valor_rb_CorteCis.get()) == 0
        and int(valor_cb_ruidoGaussiano.get()) == 0):
        valor_decimal_min_escX = valor_ent_MinEscX.get()/100
        valor_decimal_max_escX = valor_ent_MaxEscX.get()/100
        valor_decimal_min_escY = valor_ent_MinEscY.get()/100
        valor_decimal_max_escY = valor_ent_MaxEscY.get()/100
        processar.rotacaoFlipHorizontalVertical(valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY)

    #Escala, Flip Horizontal, Flip Vertical, Ruído Gaussiano
    if (int(valor_rb_TransGeo.get()) == 2 and int(valor_cb_flipHorizontal.get()) == 1
        and int(valor_cb_flipVertical.get()) == 1 and int(valor_rb_CorteCis.get()) == 0
        and int(valor_cb_ruidoGaussiano.get()) == 1):
        valor_decimal_min_escX = valor_ent_MinEscX.get()/100
        valor_decimal_max_escX = valor_ent_MaxEscX.get()/100
        valor_decimal_min_escY = valor_ent_MinEscY.get()/100
        valor_decimal_max_escY = valor_ent_MaxEscY.get()/100
        valorRuido = valor_ent_ValorRuido.get()
        valorDesvioPadrao = valor_ent_DesvPad.get()
        processar.rotacaoFlipHorizontalVerticalRuidoGaussiano(valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY, valorRuido,valorDesvioPadrao)

    #Escala, FLip Horizontal, Flip Vertical, Cisalhamento
    if (int(valor_rb_TransGeo.get()) == 2 and int(valor_cb_flipHorizontal.get()) == 1
            and int(valor_cb_flipVertical.get()) == 1 and int(valor_rb_CorteCis.get()) == 1 and int(valor_cb_ruidoGaussiano.get()) == 0):
        valor_decimal_min_escX = valor_ent_MinEscX.get()/100
        valor_decimal_max_escX = valor_ent_MaxEscX.get()/100
        valor_decimal_min_escY = valor_ent_MinEscY.get()/100
        valor_decimal_max_escY = valor_ent_MaxEscY.get()/100
        minCisalhamento = int(valor_ent_MinCis.get())
        maxCisalhamento = int(valor_ent_MaxCis.get())
        processar.escalaFlipHorizontalVerticalCisalhamento(valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY, minCisalhamento, maxCisalhamento)

    #Escala, Flip Horizontal, Flip Vertical, Corte
    if (int(valor_rb_TransGeo.get()) == 2 and int(valor_cb_flipHorizontal.get()) == 1
            and int(valor_cb_flipVertical.get()) == 1 and int(valor_rb_CorteCis.get()) == 2 and int(valor_cb_ruidoGaussiano.get()) == 0):
        valor_decimal_min_escX = valor_ent_MinEscX.get()/100
        valor_decimal_max_escX = valor_ent_MaxEscX.get()/100
        valor_decimal_min_escY = valor_ent_MinEscY.get()/100
        valor_decimal_max_escY = valor_ent_MaxEscY.get()/100
        valorDecimalCorte = int(valor_ent_Corte.get()) / 100
        processar.escalaFlipHorizontalVerticalCorte(valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY, valorDecimalCorte)

    #Escala, Flip Horizontal, Flip Vertical, Cisalhamento, Ruído Gaussiano
    if (int(valor_rb_TransGeo.get()) == 2 and int(valor_cb_flipHorizontal.get()) == 1
            and int(valor_cb_flipVertical.get()) == 1 and int(valor_rb_CorteCis.get()) == 1
            and int(valor_cb_ruidoGaussiano.get()) == 1):
        valor_decimal_min_escX = valor_ent_MinEscX.get()/100
        valor_decimal_max_escX = valor_ent_MaxEscX.get()/100
        valor_decimal_min_escY = valor_ent_MinEscY.get()/100
        valor_decimal_max_escY = valor_ent_MaxEscY.get()/100
        minCisalhamento = int(valor_ent_MinCis.get())
        maxCisalhamento = int(valor_ent_MaxCis.get())
        valorRuido = valor_ent_ValorRuido.get()
        valorDesvioPadrao = valor_ent_DesvPad.get()
        processar.escalaFlipHorizontalVerticalCisalhamentoRuidoGaussiano(valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY, minCisalhamento, maxCisalhamento, valorRuido, valorDesvioPadrao)

    #Escala, Flip Horizontal, Flip Vertical, Corte, Adição de Ruido
    if (int(valor_rb_TransGeo.get()) == 2 and int(valor_cb_flipHorizontal.get()) == 1 and int(
         valor_cb_flipVertical.get()) == 1 and int(valor_rb_CorteCis.get()) == 2 and int(
         valor_cb_ruidoGaussiano.get()) == 1):
         valor_decimal_min_escX = valor_ent_MinEscX.get()/100
         valor_decimal_max_escX = valor_ent_MaxEscX.get()/100
         valor_decimal_min_escY = valor_ent_MinEscY.get()/100
         valor_decimal_max_escY = valor_ent_MaxEscY.get()/100
         valorDecimalCorte = int(valor_ent_Corte.get()) / 100
         valorRuido = valor_ent_ValorRuido.get()
         valorDesvioPadrao = valor_ent_DesvPad.get()
         processar.escalaFlipHorizontalVerticalCorteRuidoGaussiano(valor_decimal_min_escX, valor_decimal_max_escX, valor_decimal_min_escY, valor_decimal_max_escY, valorDecimalCorte, valorRuido, valorDesvioPadrao)

#translacao
    if (int(valor_rb_TransGeo.get()) == 3 and int(valor_cb_flipHorizontal.get()) == 0 and int(valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 0 and int(valor_cb_ruidoGaussiano.get()) == 0):
        valor_decimal_min_transX = valor_ent_MinTransX.get()/100
        valor_decimal_max_transX = valor_ent_MaxTransX.get()/100
        valor_decimal_min_transY = valor_ent_MinTransY.get()/100
        valor_decimal_max_transY = valor_ent_MaxTransY.get()/100
        processar.translacao(valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY)

    #translacao, Ruido Gaussiano
    if (int(valor_rb_TransGeo.get()) == 3 and int(valor_cb_flipHorizontal.get()) == 0 and int(valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 0 and int(valor_cb_ruidoGaussiano.get()) == 1):
        valor_decimal_min_transX = valor_ent_MinTransX.get()/100
        valor_decimal_max_transX = valor_ent_MaxTransX.get()/100
        valor_decimal_min_transY = valor_ent_MinTransY.get()/100
        valor_decimal_max_transY = valor_ent_MaxTransY.get()/100
        valorRuido = valor_ent_ValorRuido.get()
        valorDesvioPadrao = valor_ent_DesvPad.get()
        processar.translacaoRuidoGaussiano(valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY, valorRuido, valorDesvioPadrao)

    #translacao,Cisalhamento
    if (int(valor_rb_TransGeo.get()) == 3 and int(valor_cb_flipHorizontal.get()) == 0 and int(valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 1 and int(valor_cb_ruidoGaussiano.get()) == 0):
        valor_decimal_min_transX = valor_ent_MinTransX.get()/100
        valor_decimal_max_transX = valor_ent_MaxTransX.get()/100
        valor_decimal_min_transY = valor_ent_MinTransY.get()/100
        valor_decimal_max_transY = valor_ent_MaxTransY.get()/100
        minCisalhamento = int(valor_ent_MinCis.get())
        maxCisalhamento = int(valor_ent_MaxCis.get())
        processar.translacaoCisalhamento(valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY, minCisalhamento, maxCisalhamento)

    #translacao,Corte
    if (int(valor_rb_TransGeo.get()) == 3 and int(valor_cb_flipHorizontal.get()) == 0 and int(valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 2 and int(valor_cb_ruidoGaussiano.get()) == 0):
        valor_decimal_min_transX = valor_ent_MinTransX.get()/100
        valor_decimal_max_transX = valor_ent_MaxTransX.get()/100
        valor_decimal_min_transY = valor_ent_MinTransY.get()/100
        valor_decimal_max_transY = valor_ent_MaxTransY.get()/100
        valorDecimalCorte = int(valor_ent_Corte.get()) / 100
        processar.translacaoCorte(valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY, valorDecimalCorte)

    #translacao, Cisalhamento, Ruido Gaussiano
    if (int(valor_rb_TransGeo.get()) == 3 and int(valor_cb_flipHorizontal.get()) == 0 and int(valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 1 and int(valor_cb_ruidoGaussiano.get()) == 1):
        valor_decimal_min_transX = valor_ent_MinTransX.get()/100
        valor_decimal_max_transX = valor_ent_MaxTransX.get()/100
        valor_decimal_min_transY = valor_ent_MinTransY.get()/100
        valor_decimal_max_transY = valor_ent_MaxTransY.get()/100
        minCisalhamento = int(valor_ent_MinCis.get())
        maxCisalhamento = int(valor_ent_MaxCis.get())
        valorRuido = valor_ent_ValorRuido.get()
        valorDesvioPadrao = valor_ent_DesvPad.get()
        processar.translacaoCisalhamentoRuidoGaussiano(valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY, minCisalhamento, maxCisalhamento, valorRuido, valorDesvioPadrao)

    #translacao, Corte, Ruido Gaussiano
    if (int(valor_rb_TransGeo.get()) == 3 and int(valor_cb_flipHorizontal.get()) == 0 and int(valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 2 and int(valor_cb_ruidoGaussiano.get()) == 1):
        valor_decimal_min_transX = valor_ent_MinTransX.get()/100
        valor_decimal_max_transX = valor_ent_MaxTransX.get()/100
        valor_decimal_min_transY = valor_ent_MinTransY.get()/100
        valor_decimal_max_transY = valor_ent_MaxTransY.get()/100
        valorDecimalCorte = int(valor_ent_Corte.get()) / 100
        valorRuido = valor_ent_ValorRuido.get()
        valorDesvioPadrao = valor_ent_DesvPad.get()
        processar.translacaoCorteRuidoGaussiano(valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY, valorDecimalCorte, valorRuido, valorDesvioPadrao)

    #Translacao, Flip Vertical
    if (int(valor_rb_TransGeo.get()) == 3 and int(valor_cb_flipHorizontal.get()) == 0
        and int(valor_cb_flipVertical.get()) == 1 and int(valor_rb_CorteCis.get()) == 0
        and int(valor_cb_ruidoGaussiano.get()) == 0):
        valor_decimal_min_transX = valor_ent_MinTransX.get()/100
        valor_decimal_max_transX = valor_ent_MaxTransX.get()/100
        valor_decimal_min_transY = valor_ent_MinTransY.get()/100
        valor_decimal_max_transY = valor_ent_MaxTransY.get()/100
        processar.translacaoFlipVertical(valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY, valor_decimal_max_escY)

    #translacao, Flip Vertical, Ruído Gaussiano
    if (int(valor_rb_TransGeo.get()) == 3 and int(valor_cb_flipHorizontal.get()) == 0
        and int(valor_cb_flipVertical.get()) == 1 and int(valor_rb_CorteCis.get()) == 0
        and int(valor_cb_ruidoGaussiano.get()) == 1):
        valor_decimal_min_transX = valor_ent_MinTransX.get()/100
        valor_decimal_max_transX = valor_ent_MaxTransX.get()/100
        valor_decimal_min_transY = valor_ent_MinTransY.get()/100
        valor_decimal_max_transY = valor_ent_MaxTransY.get()/100
        valorRuido = valor_ent_ValorRuido.get()
        valorDesvioPadrao = valor_ent_DesvPad.get()
        processar.translacaoFlipVerticalRuidoGaussiano(valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY, valorRuido,valorDesvioPadrao)

    #translacao, FLip Vertical, Cisalhamento
    if (int(valor_rb_TransGeo.get()) == 3 and int(valor_cb_flipHorizontal.get()) == 0
            and int(valor_cb_flipVertical.get()) == 1 and int(valor_rb_CorteCis.get()) == 1 and int(valor_cb_ruidoGaussiano.get()) == 0):
        valor_decimal_min_transX = valor_ent_MinTransX.get()
        valor_decimal_max_transX = valor_ent_MaxTransX.get()
        valor_decimal_min_transY = valor_ent_MinTransY.get()
        valor_decimal_max_transY = valor_ent_MaxTransY.get()
        minCisalhamento = int(valor_ent_MinCis.get())
        maxCisalhamento = int(valor_ent_MaxCis.get())
        processar.translacaoFlipVerticalCisalhamento(valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY, minCisalhamento, maxCisalhamento)

    #translacao, Flip Vertical, Corte
    if (int(valor_rb_TransGeo.get()) == 3 and int(valor_cb_flipHorizontal.get()) == 0 and int(valor_cb_flipVertical.get()) == 1 and int(valor_rb_CorteCis.get()) == 2 and int(valor_cb_ruidoGaussiano.get()) == 0):
        valor_decimal_min_transX = valor_ent_MinTransX.get()/100
        valor_decimal_max_transX = valor_ent_MaxTransX.get()/100
        valor_decimal_min_transY = valor_ent_MinTransY.get()/100
        valor_decimal_max_transY = valor_ent_MaxTransY.get()/100
        valorDecimalCorte = int(valor_ent_Corte.get()) / 100
        processar.translacaoFlipVerticalCorte(valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY, valorDecimalCorte)

    #translacao, Flip Vertical, Cisalhamento, Ruído Gaussiano
    if (int(valor_rb_TransGeo.get()) == 3 and int(valor_cb_flipHorizontal.get()) == 0 and int(valor_cb_flipVertical.get()) == 1 and int(valor_rb_CorteCis.get()) == 1 and int(valor_cb_ruidoGaussiano.get()) == 1):
        valor_decimal_min_transX = valor_ent_MinTransX.get()/100
        valor_decimal_max_transX = valor_ent_MaxTransX.get()/100
        valor_decimal_min_transY = valor_ent_MinTransY.get()/100
        valor_decimal_max_transY = valor_ent_MaxTransY.get()/100
        minCisalhamento = int(valor_ent_MinCis.get())
        maxCisalhamento = int(valor_ent_MaxCis.get())
        valorRuido = valor_ent_ValorRuido.get()
        valorDesvioPadrao = valor_ent_DesvPad.get()
        processar.translacaoFlipVerticalCisalhamentoRuidoGaussiano(valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY, minCisalhamento, maxCisalhamento, valorRuido, valorDesvioPadrao)

    #translacao, Flip Vertical, Corte, Ruido Gaussiano
    if (int(valor_rb_TransGeo.get()) == 3 and int(valor_cb_flipHorizontal.get()) == 0 and int(valor_cb_flipVertical.get()) == 1 and int(valor_rb_CorteCis.get()) == 2 and int(valor_cb_ruidoGaussiano.get()) == 1):
        valor_decimal_min_transX = valor_ent_MinTransX.get()/100
        valor_decimal_max_transX = valor_ent_MaxTransX.get()/100
        valor_decimal_min_transY = valor_ent_MinTransY.get()/100
        valor_decimal_max_transY = valor_ent_MaxTransY.get()/100
        valorDecimalCorte = int(valor_ent_Corte.get()) / 100
        valorRuido = valor_ent_ValorRuido.get()
        valorDesvioPadrao = valor_ent_DesvPad.get()
        processar.translacaoFlipVerticalCorteRuidoGaussiano(valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY, valorDecimalCorte, valorRuido, valorDesvioPadrao)

    #translacao, Flip Horizontal
    if (int(valor_rb_TransGeo.get()) == 3 and int(valor_cb_flipHorizontal.get()) == 1
        and int(valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 0
        and int(valor_cb_ruidoGaussiano.get()) == 0):
        valor_decimal_min_transX = valor_ent_MinTransX.get()/100
        valor_decimal_max_transX = valor_ent_MaxTransX.get()/100
        valor_decimal_min_transY = valor_ent_MinTransY.get()/100
        valor_decimal_max_transY = valor_ent_MaxTransY.get()/100
        processar.translacaoFlipHorizontal(valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY)

    #translacao, Flip Horizontal, Ruído Gaussiano
    if (int(valor_rb_TransGeo.get()) == 3 and int(valor_cb_flipHorizontal.get()) == 1
        and int(valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 0
        and int(valor_cb_ruidoGaussiano.get()) == 1):
        valor_decimal_min_transX = valor_ent_MinTransX.get()/100
        valor_decimal_max_transX = valor_ent_MaxTransX.get()/100
        valor_decimal_min_transY = valor_ent_MinTransY.get()/100
        valor_decimal_max_transY = valor_ent_MaxTransY.get()/100
        valorRuido = valor_ent_ValorRuido.get()
        valorDesvioPadrao = valor_ent_DesvPad.get()
        processar.escalaFlipHorizontalRuidoGaussiano(valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY, valorRuido,valorDesvioPadrao)

    #translacao, FLip Horizontal, Cisalhamento
    if (int(valor_rb_TransGeo.get()) == 3 and int(valor_cb_flipHorizontal.get()) == 1 and int(valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 1 and int(valor_cb_ruidoGaussiano.get()) == 0):
        valor_decimal_min_transX = valor_ent_MinTransX.get()/100
        valor_decimal_max_transX = valor_ent_MaxTransX.get()/100
        valor_decimal_min_transY = valor_ent_MinTransY.get()/100
        valor_decimal_max_transY = valor_ent_MaxTransY.get()/100
        minCisalhamento = int(valor_ent_MinCis.get())
        maxCisalhamento = int(valor_ent_MaxCis.get())
        processar.escalaFlipHorizontalCisalhamento(valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY, minCisalhamento, maxCisalhamento)

    #translacao, Flip Horizontal, Corte
    if (int(valor_rb_TransGeo.get()) == 3 and int(valor_cb_flipHorizontal.get()) == 1 and int(valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 2 and int(valor_cb_ruidoGaussiano.get()) == 0):
        valor_decimal_min_transX = valor_ent_MinTransX.get()/100
        valor_decimal_max_transX = valor_ent_MaxTransX.get()/100
        valor_decimal_min_transY = valor_ent_MinTransY.get()/100
        valor_decimal_max_transY = valor_ent_MaxTransY.get()/100
        valorDecimalCorte = int(valor_ent_Corte.get()) / 100
        processar.translacaoFlipHorizontalCorte(valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY, valorDecimalCorte)

    #translacao, Flip Horizontal, Cisalhamento, Ruído Gaussiano
    if (int(valor_rb_TransGeo.get()) == 3 and int(valor_cb_flipHorizontal.get()) == 1 and int(valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 1 and int(valor_cb_ruidoGaussiano.get()) == 1):
        valor_decimal_min_transX = valor_ent_MinTransX.get()/100
        valor_decimal_max_transX = valor_ent_MaxTransX.get()/100
        valor_decimal_min_transY = valor_ent_MinTransY.get()/100
        valor_decimal_max_transY = valor_ent_MaxTransY.get()/100
        minCisalhamento = int(valor_ent_MinCis.get())
        maxCisalhamento = int(valor_ent_MaxCis.get())
        valorRuido = valor_ent_ValorRuido.get()
        valorDesvioPadrao = valor_ent_DesvPad.get()
        processar.translacaoFlipHorizontalCisalhamentoRuidoGaussiano(valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY, minCisalhamento, maxCisalhamento, valorRuido, valorDesvioPadrao)

    # translacao, Flip Horizontal, Corte, Adição de Ruido
    if (int(valor_rb_TransGeo.get()) == 3 and int(valor_cb_flipHorizontal.get()) == 1 and int(
         valor_cb_flipVertical.get()) == 0 and int(valor_rb_CorteCis.get()) == 2 and int(
         valor_cb_ruidoGaussiano.get()) == 1):
         valor_decimal_min_transX = valor_ent_MinTransX.get()/100
         valor_decimal_max_transX = valor_ent_MaxTransX.get()/100
         valor_decimal_min_transY = valor_ent_MinTransY.get()/100
         valor_decimal_max_transY = valor_ent_MaxTransY.get()/100
         valorDecimalCorte = int(valor_ent_Corte.get()) / 100
         valorRuido = valor_ent_ValorRuido.get()
         valorDesvioPadrao = valor_ent_DesvPad.get()
         processar.translacaoFlipHorizontalCorteRuidoGaussiano(valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY, valorDecimalCorte, valorRuido, valorDesvioPadrao)

#translacao, Flip Horizontal, Flip Vertical
    if (int(valor_rb_TransGeo.get()) == 3 and int(valor_cb_flipHorizontal.get()) == 1
        and int(valor_cb_flipVertical.get()) == 1 and int(valor_rb_CorteCis.get()) == 0
        and int(valor_cb_ruidoGaussiano.get()) == 0):
        valor_decimal_min_transX = valor_ent_MinTransX.get()/100
        valor_decimal_max_transX = valor_ent_MaxTransX.get()/100
        valor_decimal_min_transY = valor_ent_MinTransY.get()/100
        valor_decimal_max_transY = valor_ent_MaxTransY.get()/100
        processar.rotacaoFlipHorizontalVertical(valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY)

    #translacao, Flip Horizontal, Flip Vertical, Ruído Gaussiano
    if (int(valor_rb_TransGeo.get()) == 3 and int(valor_cb_flipHorizontal.get()) == 1
        and int(valor_cb_flipVertical.get()) == 1 and int(valor_rb_CorteCis.get()) == 0
        and int(valor_cb_ruidoGaussiano.get()) == 1):
        valor_decimal_min_transX = valor_ent_MinTransX.get()/100
        valor_decimal_max_transX = valor_ent_MaxTransX.get()/100
        valor_decimal_min_transY = valor_ent_MinTransY.get()/100
        valor_decimal_max_transY = valor_ent_MaxTransY.get()/100
        valorRuido = valor_ent_ValorRuido.get()
        valorDesvioPadrao = valor_ent_DesvPad.get()
        processar.translacaoFlipHorizontalVerticalRuidoGaussiano(valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY, valorRuido,valorDesvioPadrao)

    #translacao, FLip Horizontal, Flip Vertical, Cisalhamento
    if (int(valor_rb_TransGeo.get()) == 3 and int(valor_cb_flipHorizontal.get()) == 1
            and int(valor_cb_flipVertical.get()) == 1 and int(valor_rb_CorteCis.get()) == 1 and int(valor_cb_ruidoGaussiano.get()) == 0):
        valor_decimal_min_transX = valor_ent_MinTransX.get()/100
        valor_decimal_max_transX = valor_ent_MaxTransX.get()/100
        valor_decimal_min_transY = valor_ent_MinTransY.get()/100
        valor_decimal_max_transY = valor_ent_MaxTransY.get()/100
        minCisalhamento = int(valor_ent_MinCis.get())
        maxCisalhamento = int(valor_ent_MaxCis.get())
        processar.translacaoFlipHorizontalVerticalCisalhamento(valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY, minCisalhamento, maxCisalhamento)

    #translacao, Flip Horizontal, Flip Vertical, Corte
    if (int(valor_rb_TransGeo.get()) == 3 and int(valor_cb_flipHorizontal.get()) == 1
            and int(valor_cb_flipVertical.get()) == 1 and int(valor_rb_CorteCis.get()) == 2 and int(valor_cb_ruidoGaussiano.get()) == 0):
        valor_decimal_min_transX = valor_ent_MinTransX.get()/100
        valor_decimal_max_transX = valor_ent_MaxTransX.get()/100
        valor_decimal_min_transY = valor_ent_MinTransY.get()/100
        valor_decimal_max_transY = valor_ent_MaxTransY.get()/100
        valorDecimalCorte = int(valor_ent_Corte.get()) / 100
        processar.translacaoFlipHorizontalVerticalCorte(valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY, valorDecimalCorte)

    #translacao, Flip Horizontal, Flip Vertical, Cisalhamento, Ruído Gaussiano
    if (int(valor_rb_TransGeo.get()) == 3 and int(valor_cb_flipHorizontal.get()) == 1
            and int(valor_cb_flipVertical.get()) == 1 and int(valor_rb_CorteCis.get()) == 1
            and int(valor_cb_ruidoGaussiano.get()) == 1):
        valor_decimal_min_transX = valor_ent_MinTransX.get()/100
        valor_decimal_max_transX = valor_ent_MaxTransX.get()/100
        valor_decimal_min_transY = valor_ent_MinTransY.get()/100
        valor_decimal_max_transY = valor_ent_MaxTransY.get()/100
        minCisalhamento = int(valor_ent_MinCis.get())
        maxCisalhamento = int(valor_ent_MaxCis.get())
        valorRuido = valor_ent_ValorRuido.get()
        valorDesvioPadrao = valor_ent_DesvPad.get()
        processar.translacaoFlipHorizontalVerticalCisalhamentoRuidoGaussiano(valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY, minCisalhamento, maxCisalhamento, valorRuido, valorDesvioPadrao)

    #translacao, Flip Horizontal, Flip Vertical, Corte, Adição de Ruido
    if (int(valor_rb_TransGeo.get()) == 3 and int(valor_cb_flipHorizontal.get()) == 1 and int(
         valor_cb_flipVertical.get()) == 1 and int(valor_rb_CorteCis.get()) == 2 and int(
         valor_cb_ruidoGaussiano.get()) == 1):
         valor_decimal_min_transX = valor_ent_MinTransX.get()/100
         valor_decimal_max_transX = valor_ent_MaxTransX.get()/100
         valor_decimal_min_transY = valor_ent_MinTransY.get()/100
         valor_decimal_max_transY = valor_ent_MaxTransY.get()/100
         valorDecimalCorte = int(valor_ent_Corte.get()) / 100
         valorRuido = valor_ent_ValorRuido.get()
         valorDesvioPadrao = valor_ent_DesvPad.get()
         processar.translacaoFlipHorizontalVerticalCorteRuidoGaussiano(valor_decimal_min_transX, valor_decimal_max_transX, valor_decimal_min_transY, valor_decimal_max_transY, valorDecimalCorte, valorRuido, valorDesvioPadrao)


#funções de abrir diretórios

def abrirDiretorioEntrada():
    global dirEntrada
    dirEntrada = filedialog.askdirectory()

def abrirDiretorioSaida():
    global dirSaida
    dirSaida = filedialog.askdirectory()

#funções de abrir telas

def abrirTransformacoesGeometricas():
    frameTransformacoesGeometricas = tk.Toplevel()

    #Dividindo tela
    frameCimaTransformacoesGeometricas = Frame(frameTransformacoesGeometricas, width=550, height=42, bg=cor1, relief='flat')
    frameCimaTransformacoesGeometricas.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

    frameBaixoTransformacoesGeometricas = Frame(frameTransformacoesGeometricas, width=550, height=270, bg=cor1, relief='flat')
    frameBaixoTransformacoesGeometricas.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

    #Subdividindo Frame Baixo

    frameParteUmTransformacoesGeometricas = Frame(frameBaixoTransformacoesGeometricas, width=550, height=30, bg=cor1, relief='flat')
    frameParteUmTransformacoesGeometricas.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

    frameParteDoisTransformacoesGeometricas = Frame(frameBaixoTransformacoesGeometricas, width=550, height=40, bg=cor1, relief='flat', highlightbackground=cor2, highlightthickness=5)
    frameParteDoisTransformacoesGeometricas.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

    frameParteTresTransformacoesGeometricas = Frame(frameBaixoTransformacoesGeometricas, width=550, height=40, bg=cor1, relief='flat', highlightbackground=cor2, highlightthickness=5)
    frameParteTresTransformacoesGeometricas.grid(row=2, column=0, pady=1, padx=0, sticky=NSEW)

    frameParteQuatroTransformacoesGeometricas = Frame(frameBaixoTransformacoesGeometricas, width=550, height=68, bg=cor1, relief='flat', highlightbackground=cor2, highlightthickness=5)
    frameParteQuatroTransformacoesGeometricas.grid(row=3, column=0, pady=1, padx=0, sticky=NSEW)

    frameParteCincoTransformacoesGeometricas = Frame(frameBaixoTransformacoesGeometricas, width=550, height=68, bg=cor1, relief='flat', highlightbackground=cor2, highlightthickness=5)
    frameParteCincoTransformacoesGeometricas.grid(row=4, column=0, pady=1, padx=0, sticky=NSEW)


    #Configurando Frame Cima
    lb_nome = Label(frameCimaTransformacoesGeometricas, text='Data Augmentation System', anchor=NE, font=('Ivy 18'), bg=cor1, fg=cor4)
    lb_nome.place(x=0, y=5)

    lb_linha = Label(frameCimaTransformacoesGeometricas, text='', width=310, anchor=NE, font=('Ivy 1'), bg=cor2, fg=cor4)
    lb_linha.place(x=5, y=35)

    #Configurando Frame Baixo Parte 1

    lb_selecioneTransformacao = Label(frameParteUmTransformacoesGeometricas, text='Selecione a transformação:', anchor=CENTER, font=('Ivy 12 bold'),
                         bg=cor1, fg=cor4)
    lb_selecioneTransformacao.place(x=160, y=2)

    #Configurando Frame Baixo Parte 2
    rb_rotacao = Radiobutton(frameParteDoisTransformacoesGeometricas, text="Rotação",
                                 variable=valor_rb_TransGeo,
                                 value=1, anchor=CENTER, font=('Ivy 8 bold'),
                         bg=cor1, fg=cor4)
    rb_rotacao.place(x=15, y=3)

    lb_rotacaoAnguloMinimo = Label(frameParteDoisTransformacoesGeometricas, text='Ângulo Mínimo:', anchor=NE, font=('Ivy 8 bold'),
                    bg=cor1, fg=cor4)
    lb_rotacaoAnguloMinimo.place(x=150, y=5)

    ent_rotacaoAnguloMinimo = Entry(frameParteDoisTransformacoesGeometricas, width=10, textvariable=valor_ent_MinRot)
    ent_rotacaoAnguloMinimo.place(x=250, y=5)

    lb_rotacaoAnguloMaximo = Label(frameParteDoisTransformacoesGeometricas, text='Ângulo Máximo:', anchor=NE, font=('Ivy 8 bold'),
                                   bg=cor1, fg=cor4)
    lb_rotacaoAnguloMaximo.place(x=350, y=5)

    ent_rotacaoAnguloMaximo = Entry(frameParteDoisTransformacoesGeometricas, width=10, textvariable=valor_ent_MaxRot)
    ent_rotacaoAnguloMaximo.place(x=450, y=5)

    # Configurando Frame Baixo Parte 3
    cb_flipVertical = Checkbutton(frameParteTresTransformacoesGeometricas, text="Flip Vertical",
                             variable=valor_cb_flipVertical,
                             anchor=CENTER, font=('Ivy 8 bold'),
                             bg=cor1, fg=cor4)
    cb_flipVertical.place(x=150, y=3)

    cb_flipHorizontal = Checkbutton(frameParteTresTransformacoesGeometricas, text="Flip Horizontal",
                                  variable=valor_cb_flipHorizontal,
                                  anchor=CENTER, font=('Ivy 8 bold'),
                                  bg=cor1, fg=cor4)
    cb_flipHorizontal.place(x=350, y=3)

    # Configurando Frame Baixo Parte 4
    rb_escala = Radiobutton(frameParteQuatroTransformacoesGeometricas, text="Escala",
                             variable=valor_rb_TransGeo,
                             value=2, anchor=CENTER, font=('Ivy 8 bold'),
                             bg=cor1, fg=cor4)
    rb_escala.place(x=15, y=3)

    lb_escalaMinimoX = Label(frameParteQuatroTransformacoesGeometricas, text='Mínimo Escala (X):', anchor=NE, font=('Ivy 8 bold'),
                                   bg=cor1, fg=cor4)
    lb_escalaMinimoX.place(x=149, y=5)

    ent_escalaMinimoX = Entry(frameParteQuatroTransformacoesGeometricas, width=10, textvariable=valor_ent_MinEscX)
    ent_escalaMinimoX.place(x=251, y=5)

    lb_escalaMaximoX = Label(frameParteQuatroTransformacoesGeometricas, text='Máximo Escala (X):', anchor=NE, font=('Ivy 8 bold'),
                                   bg=cor1, fg=cor4)
    lb_escalaMaximoX.place(x=350, y=5)

    ent_escalaMaximoX = Entry(frameParteQuatroTransformacoesGeometricas, width=10, textvariable=valor_ent_MaxEscX)
    ent_escalaMaximoX.place(x=455, y=5)

    lb_escalaMinimoY = Label(frameParteQuatroTransformacoesGeometricas, text='Mínimo Escala (Y):', anchor=NE, font=('Ivy 8 bold'),
                             bg=cor1, fg=cor4)
    lb_escalaMinimoY.place(x=149, y=25)

    ent_escalaMinimoY = Entry(frameParteQuatroTransformacoesGeometricas, width=10, textvariable=valor_ent_MinEscY)
    ent_escalaMinimoY.place(x=251, y=25)

    lb_escalaMaximoY = Label(frameParteQuatroTransformacoesGeometricas, text='Máximo Escala (Y):', anchor=NE, font=('Ivy 8 bold'),
                             bg=cor1, fg=cor4)
    lb_escalaMaximoY.place(x=350, y=25)

    ent_escalaMaximoX = Entry(frameParteQuatroTransformacoesGeometricas, width=10, textvariable=valor_ent_MaxEscY)
    ent_escalaMaximoX.place(x=455, y=25)

    # Configurando Frame Baixo Parte 5
    rb_translacao = Radiobutton(frameParteCincoTransformacoesGeometricas, text="Translação",
                            variable=valor_rb_TransGeo,
                            value=3, anchor=CENTER, font=('Ivy 8 bold'),
                            bg=cor1, fg=cor4)
    rb_translacao.place(x=15, y=3)

    lb_translacaoMinimoX = Label(frameParteCincoTransformacoesGeometricas, text='Mínimo Transl. (X):', anchor=NE, font=('Ivy 8 bold'),
                             bg=cor1, fg=cor4)
    lb_translacaoMinimoX.place(x=149, y=5)

    ent_translacaoMinimoX = Entry(frameParteCincoTransformacoesGeometricas, width=10, textvariable=valor_ent_MinTransX)
    ent_translacaoMinimoX.place(x=251, y=5)

    lb_translacaoMaximoX = Label(frameParteCincoTransformacoesGeometricas, text='Máximo Transl. (X):', anchor=NE, font=('Ivy 8 bold'),
                             bg=cor1, fg=cor4)
    lb_translacaoMaximoX.place(x=350, y=5)

    ent_translacaoMaximoX = Entry(frameParteCincoTransformacoesGeometricas, width=10, textvariable=valor_ent_MaxTransX)
    ent_translacaoMaximoX.place(x=455, y=5)

    lb_translacaoMinimoY = Label(frameParteCincoTransformacoesGeometricas, text='Mínimo Transl. (Y):', anchor=NE, font=('Ivy 8 bold'),
                             bg=cor1, fg=cor4)
    lb_translacaoMinimoY.place(x=149, y=25)

    ent_translacaoMinimoY = Entry(frameParteCincoTransformacoesGeometricas, width=10, textvariable=valor_ent_MinTransY)
    ent_translacaoMinimoY.place(x=251, y=25)

    lb_translacaoMaximoY = Label(frameParteCincoTransformacoesGeometricas, text='Máximo Transl. (Y):', anchor=NE, font=('Ivy 8 bold'),
                             bg=cor1, fg=cor4)
    lb_translacaoMaximoY.place(x=350, y=25)

    ent_translacaoMaximoX = Entry(frameParteCincoTransformacoesGeometricas, width=10, textvariable=valor_ent_MaxTransY)
    ent_translacaoMaximoX.place(x=455, y=25)

def abrirCorteCisalhamento():
    frameCorteCisalhamento = tk.Toplevel()

    # Dividindo tela
    frameCimaTransformacoesGeometricas = Frame(frameCorteCisalhamento, width=550, height=42, bg=cor1, relief='flat')
    frameCimaTransformacoesGeometricas.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

    frameBaixoTransformacoesGeometricas = Frame(frameCorteCisalhamento, width=550, height=270, bg=cor1, relief='flat')
    frameBaixoTransformacoesGeometricas.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

    # Subdividindo Frame Baixo

    frameParteUmCorteCisalhamento = Frame(frameBaixoTransformacoesGeometricas, width=550, height=30, bg=cor1,
                                                  relief='flat')
    frameParteUmCorteCisalhamento.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

    frameParteDoisCorteCisalhamento = Frame(frameBaixoTransformacoesGeometricas, width=550, height=100, bg=cor1,
                                                    relief='flat', highlightbackground=cor2, highlightthickness=5)
    frameParteDoisCorteCisalhamento.grid(row=1, column=0, pady=5, padx=0, sticky=NSEW)

    frameParteTresCorteCisalhamento = Frame(frameBaixoTransformacoesGeometricas, width=550, height=100, bg=cor1,
                                                    relief='flat', highlightbackground=cor2, highlightthickness=5)
    frameParteTresCorteCisalhamento.grid(row=2, column=0, pady=5, padx=0, sticky=NSEW)

    # Configurando Frame Cima
    lb_nome = Label(frameCimaTransformacoesGeometricas, text='Data Augmentation System', anchor=NE, font=('Ivy 18'),
                    bg=cor1, fg=cor4)
    lb_nome.place(x=0, y=5)

    lb_linha = Label(frameCimaTransformacoesGeometricas, text='', width=310, anchor=NE, font=('Ivy 1'), bg=cor2,
                     fg=cor4)
    lb_linha.place(x=5, y=35)

    # Configurando Frame Baixo Parte 1
    lb_corteCisalhamento = Label(frameParteUmCorteCisalhamento, text='Corte e Cisalhamento',
                                      anchor=CENTER, font=('Ivy 12 bold'),
                                      bg=cor1, fg=cor4)
    lb_corteCisalhamento.place(x=200, y=2)

    # Configurando Frame Baixo Parte 2
    rb_Cisalhamento = Radiobutton(frameParteDoisCorteCisalhamento,
                                  text="Cisalhamento",
                                  variable=valor_rb_CorteCis,
                                  value=1, anchor=CENTER, font=('Ivy 8 bold'),
                         bg=cor1, fg=cor4)
    rb_Cisalhamento.place(x=15, y=35)

    lb_cisalhamentoAnguloMinimo = Label(frameParteDoisCorteCisalhamento, text="Ângulo Mínimo: ", anchor=NE, font=('Ivy 8 bold'),
                             bg=cor1, fg=cor4)
    lb_cisalhamentoAnguloMinimo.place(x=150, y=35)

    ent_cisalhamentoAnguloMinimo = Entry(frameParteDoisCorteCisalhamento, width=10, textvariable=valor_ent_MinCis)
    ent_cisalhamentoAnguloMinimo.place(x=250, y=35)

    lb_cisalhamentoAnguloMaximo = Label(frameParteDoisCorteCisalhamento, text="Ângulo Máximo: ", anchor=NE, font=('Ivy 8 bold'),
                             bg=cor1, fg=cor4)
    lb_cisalhamentoAnguloMaximo.place(x=350, y=35)

    ent_cisalhamentoAnguloMaximo = Entry(frameParteDoisCorteCisalhamento, width=10, textvariable=valor_ent_MaxCis)
    ent_cisalhamentoAnguloMaximo.place(x=450, y=35)

    # Configurando Frame Baixo Parte 3
    rb_corte = Radiobutton(frameParteTresCorteCisalhamento,
                                  text="Corte",
                                  variable=valor_rb_CorteCis,
                                  value=2, anchor=CENTER, font=('Ivy 8 bold'),
                                  bg=cor1, fg=cor4)
    rb_corte.place(x=15, y=35)

    lb_corte = Label(frameParteTresCorteCisalhamento, text="Relação Altura/Largura:", anchor=NE,
                                        font=('Ivy 8 bold'),
                                        bg=cor1, fg=cor4)
    lb_corte.place(x=150, y=35)

    ent_corte = Entry(frameParteTresCorteCisalhamento, width=10, textvariable=valor_ent_Corte)
    ent_corte.place(x=300, y=35)

def abirAdicaoRuido():


    frameAdicaoRuido = tk.Toplevel()

    # Dividindo tela
    frameCimaAdicaoRuido = Frame(frameAdicaoRuido, width=550, height=42, bg=cor1, relief='flat')
    frameCimaAdicaoRuido.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

    frameBaixoAdicaoRuido = Frame(frameAdicaoRuido, width=550, height=270, bg=cor1, relief='flat')
    frameBaixoAdicaoRuido.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

    # Subdividindo Frame Baixo

    frameParteUmAdicaoRuido = Frame(frameBaixoAdicaoRuido, width=550, height=30, bg=cor1,
                                                  relief='flat')
    frameParteUmAdicaoRuido.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

    frameParteDoisAdicaoRuido = Frame(frameBaixoAdicaoRuido, width=550, height=100, bg=cor1,
                                                    relief='flat', highlightbackground=cor2, highlightthickness=5)
    frameParteDoisAdicaoRuido.grid(row=1, column=0, pady=5, padx=0, sticky=NSEW)

    # Configurando Frame Cima
    lb_nome = Label(frameCimaAdicaoRuido, text='Data Augmentation System', anchor=NE, font=('Ivy 18'),
                    bg=cor1, fg=cor4)
    lb_nome.place(x=0, y=5)

    lb_linha = Label(frameCimaAdicaoRuido, text='', width=310, anchor=NE, font=('Ivy 1'), bg=cor2,
                     fg=cor4)
    lb_linha.place(x=5, y=35)

    # Configurando Frame Baixo Parte 1
    lb_adicaoRuido = Label(frameParteUmAdicaoRuido, text='Adição de Ruído',
                                 anchor=CENTER, font=('Ivy 12 bold'),
                                 bg=cor1, fg=cor4)
    lb_adicaoRuido.place(x=220, y=2)

    # Configurando Frame Baixo Parte 1
    cb_adicaoRuido = Checkbutton(frameParteDoisAdicaoRuido, text="Ruído Gaussiano",
                             variable=valor_cb_ruidoGaussiano,
                             anchor=CENTER, font=('Ivy 8 bold'),
                             bg=cor1, fg=cor4)
    cb_adicaoRuido.place(x=0, y=30)

    lb_desvioPadrao = Label(frameParteDoisAdicaoRuido, text='Desvio Padrão:', anchor=NE,
                                   font=('Ivy 8 bold'),
                                   bg=cor1, fg=cor4)
    lb_desvioPadrao.place(x=150, y=30)

    ent_desvioPadrao = Entry(frameParteDoisAdicaoRuido, width=10, textvariable=valor_ent_DesvPad)
    ent_desvioPadrao.place(x=250, y=30)

    lb_valorRuido = Label(frameParteDoisAdicaoRuido, text='Valor Ruído:', anchor=NE,
                                   font=('Ivy 8 bold'),
                                   bg=cor1, fg=cor4)
    lb_valorRuido.place(x=350, y=30)

    ent_valorRuido = Entry(frameParteDoisAdicaoRuido, width=10, textvariable=valor_ent_ValorRuido)
    ent_valorRuido.place(x=450, y=30)



#Classes e Telas

telaInicial = tk.Tk()
telaInicial.title('DAS - Data Augmentation System')
telaInicial.geometry('550x300')
telaInicial.configure(background=cor1)

#Variáveis

valor_rb_TransGeo = IntVar()
valor_ent_MinRot = IntVar()
valor_ent_MaxRot = IntVar()
valor_cb_flipVertical = IntVar()
valor_cb_flipHorizontal = IntVar()
valor_ent_MinEscX = IntVar()
valor_ent_MaxEscX = IntVar()
valor_ent_MinEscY = IntVar()
valor_ent_MaxEscY = IntVar()
valor_ent_MinTransX = IntVar()
valor_ent_MaxTransX = IntVar()
valor_ent_MinTransY = IntVar()
valor_ent_MaxTransY = IntVar()

valor_rb_CorteCis = IntVar()
valor_ent_MinCis = IntVar()
valor_ent_MaxCis = IntVar()
valor_ent_Corte = IntVar()

valor_cb_ruidoGaussiano = IntVar()
valor_ent_ValorRuido = IntVar()
valor_ent_DesvPad = IntVar()


#Dividindo a janela.....
frameCimaTelaInicial = Frame(telaInicial, width=550,height=42,bg=cor1,relief='flat')
frameCimaTelaInicial.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frameBaixoTelaInicial= Frame(telaInicial, width=550, height=270, bg=cor1, relief='flat')
frameBaixoTelaInicial.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

#Subdividindo a parte de baixo
frameEsquerdaBaixoTelaInicial = Frame(frameBaixoTelaInicial, width=275,height=250,bg=cor1,relief='flat', highlightbackground=cor2, highlightthickness=5)
frameEsquerdaBaixoTelaInicial.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frameDireitaBaixoTelaInicial = Frame(frameBaixoTelaInicial, width=275,height=250,bg=cor1,relief='flat')
frameDireitaBaixoTelaInicial.grid(row=0, column=1, pady=1, padx=0, sticky=NSEW)

#Subdividindo a parte direita da parte de baixo
frameParteCimaDireitaBaixoTelaInicial = Frame(frameDireitaBaixoTelaInicial, width=275,height=127,bg=cor1,relief='flat', highlightbackground=cor2, highlightthickness=5 )
frameParteCimaDireitaBaixoTelaInicial.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

frameParteBaixoDireitaBaixoTelaInicial = Frame(frameDireitaBaixoTelaInicial, width=275,height=127,bg=cor1,relief='flat', highlightbackground=cor2, highlightthickness=5 )
frameParteBaixoDireitaBaixoTelaInicial.grid(row=1, column=0, pady=0, padx=0, sticky=NSEW)

#Configurando Frame Cima..........
lb_nome = Label(frameCimaTelaInicial, text='Data Augmentation System', anchor=NE, font=('Ivy 18'), bg=cor1, fg=cor4)
lb_nome.place(x=0, y=5)

lb_linha = Label(frameCimaTelaInicial, text='', width=310, anchor=NE, font=('Ivy 1'), bg=cor2, fg=cor4)
lb_linha.place(x=5, y=35)


#Configuraando Frame Baixo Lado Esquerdo.......
lb_escolhaTransformacao = Label(frameEsquerdaBaixoTelaInicial, text='Escolha a transformação', anchor=CENTER, font=('Ivy 8 bold'), bg=cor1, fg=cor4)
lb_escolhaTransformacao.place(x=60, y=2)

bt_transformacaoGeometrica = Button(frameEsquerdaBaixoTelaInicial, command=abrirTransformacoesGeometricas, text='Transformação Geométrica', width=35, height=2, bg=cor2, fg=cor1, font=('Ivy 6 bold'), relief=RAISED, overrelief=RIDGE)
bt_transformacaoGeometrica.place(x=40, y=60)

bt_CorteCisalhamento = Button(frameEsquerdaBaixoTelaInicial, text='Corte/Cisalhamento', command=abrirCorteCisalhamento, width=35, height=2, bg=cor2, fg=cor1, font=('Ivy 6 bold'), relief=RAISED, overrelief=RIDGE)
bt_CorteCisalhamento.place(x=40, y=120)

bt_adicaoRuido = Button(frameEsquerdaBaixoTelaInicial, text='Adição de Ruído', command=abirAdicaoRuido, width=35, height=2, bg=cor2, fg=cor1, font=('Ivy 6 bold'), relief=RAISED, overrelief=RIDGE)
bt_adicaoRuido.place(x=40, y=180)

#Configurando Frame Parte de Cima da Parte Direita da Parte de Baixo da Tela Inicial
lb_diretorio = Label(frameParteCimaDireitaBaixoTelaInicial, text='Diretórios:', anchor=CENTER, font=('Ivy 8 bold'), bg=cor1, fg=cor4)
lb_diretorio.place(x=108, y=2)

lb_pastaEntrada = Label(frameParteCimaDireitaBaixoTelaInicial, text='Pasta Entrada:', anchor=CENTER, font=('Ivy 8 bold'), bg=cor1, fg=cor4)
lb_pastaEntrada.place(x=25, y=30)

bt_pastaEntrada = Button(frameParteCimaDireitaBaixoTelaInicial, text='Browse', width=15, height=2, bg=cor2, fg=cor1, font=('Ivy 6 bold'), relief=RAISED, overrelief=RIDGE, command=abrirDiretorioEntrada)
bt_pastaEntrada.place(x=25, y=60)

lb_pastaSaida = Label(frameParteCimaDireitaBaixoTelaInicial, text='Pasta Saída:', anchor=CENTER, font=('Ivy 8 bold'), bg=cor1, fg=cor4)
lb_pastaSaida.place(x=170, y=30)

bt_pastaSaida = Button(frameParteCimaDireitaBaixoTelaInicial, text='Browse', width=15, height=2, bg=cor2, fg=cor1, font=('Ivy 6 bold'), relief=RAISED, overrelief=RIDGE, command=abrirDiretorioSaida)
bt_pastaSaida.place(x=164, y=60)

#Configurando Frame Parte de Baixo da Parte Direita da Parte de Baixo da Tela Inicial
lb_quantidade = Label(frameParteBaixoDireitaBaixoTelaInicial, text='Imagens a serem geradas:', anchor=CENTER, font=('Ivy 8 bold'), bg=cor1, fg=cor4)
lb_quantidade.place(x=20, y=2)

ent_quantidade = Entry(frameParteBaixoDireitaBaixoTelaInicial, width=10)
ent_quantidade.place(x=180, y=2)

bt_iniciar = Button(frameParteBaixoDireitaBaixoTelaInicial, text='Iniciar', width=15, height=2, bg=cor2, fg=cor1, font=('Ivy 6 bold'), relief=RAISED, overrelief=RIDGE, command=iniciarDataAugmentation)
bt_iniciar.place(x=95, y=60)

telaInicial.mainloop()



"""
class FrameTransGeo(Toplevel):

    def __init__(self, parent):
        super().__init__()
        self.title("DAS - Transformações Geométricas")
        lb_Titulo = Label(self,
                          text="Selecione uma opção de transformação geométrica",
                          font='Times 14 bold',
                          anchor=CENTER)
        rb_Rotacao = Radiobutton(self,
                                 text="Rotação",
                                 variable=valor_rb_TransGeo,
                                 value=1,
                                 )
        lb_MinRot = Label(self, text="Menor ângulo possível de rotação:")
        ent_MinRot = Entry(self, textvariable=valor_ent_MinRot)
        lb_MaxRot = Label(self, text="Maior ângulo possível de rotação:")
        ent_MaxRot = Entry(self, textvariable=valor_ent_MaxRot)
        rb_FlipVert = Radiobutton(self,
                                  text="Flip Vertical",
                                  variable=valor_rb_TransGeo,
                                  value=2,
                                  )
        lb_FlipVert = Label(self, text="% Chance de ocorrer o Flip Vertical:")
        ent_FlipVert = Entry(self, textvariable=valor_ent_FlipVert)
        rb_FlipHoriz = Radiobutton(self,
                                   text="Flip Horizontal",
                                   variable=valor_rb_TransGeo,
                                   value=3,
                                   )
        lb_FlipHoriz = Label(self, text="% Chance de ocorrer o Flip Horizontal:")
        ent_FlipHoriz = Entry(self, textvariable=valor_ent_FlipHoriz)
        rb_Escala = Radiobutton(self,
                                text="Escala",
                                variable=valor_rb_TransGeo,
                                value=4,
                                )
        lb_MinEscX = Label(self, text="Menor Valor Multiplicador da escala no eixo x:")
        ent_MinEscX = Entry(self, textvariable=valor_ent_MinEscX)
        lb_MaxEscX = Label(self, text="Maior Valor Multiplicador de escala no eixo x:")
        ent_MaxEscX = Entry(self, textvariable=valor_ent_MaxEscX)
        lb_MinEscY = Label(self, text="Menor Valor Multiplicador da escala no eixo y:")
        ent_MinEscY = Entry(self, textvariable=valor_ent_MinEscY)
        lb_MaxEscY = Label(self, text="Maior Valor Multiplicador de escala no eixo y:")
        ent_MaxEscY = Entry(self, textvariable=valor_ent_MaxEscY)
        rb_Transladar = Radiobutton(self,
                                    text="Transladar",
                                    variable=valor_rb_TransGeo,
                                    value=5,
                                    )
        lb_MinTransX = Label(self, text="% Minima para transladar no eixo x:")
        ent_MinTransX = Entry(self, textvariable=valor_ent_MinTransX)
        lb_MaxTransX = Label(self, text="% Máxima para transladar no eixo x:")
        ent_MaxTransX = Entry(self, textvariable=valor_ent_MaxTransX)
        lb_MinTransY = Label(self, text="% Mínima para transladar no eixo y:")
        ent_MinTransY = Entry(self, textvariable=valor_ent_MinTransY)
        lb_MaxTransY = Label(self, text="% Máxima para transladar no eixo y:")
        ent_MaxTransY = Entry(self, textvariable=valor_ent_MaxTransY)
        bt_Salvar = Button(self, text="Salvar", command=salvarTransformacaoGeometrica)

        lb_Titulo.grid(row=0, columnspan=5)
        rb_Rotacao.grid(row=1, column=0, sticky=W)
        lb_MinRot.grid(row=1, column=1)
        ent_MinRot.grid(row=1, column=2)
        lb_MaxRot.grid(row=2, column=1)
        ent_MaxRot.grid(row=2, column=2)
        rb_FlipVert.grid(row=3, column=0, sticky=W)
        lb_FlipVert.grid(row=3, column=1)
        ent_FlipVert.grid(row=3, column=2)
        rb_FlipHoriz.grid(sticky=W)
        lb_FlipHoriz.grid(row=4, column=1)
        ent_FlipHoriz.grid(row=4, column=2)
        rb_Escala.grid(row=5, column=0, sticky=W)
        lb_MinEscX.grid(row=5, column=1)
        ent_MinEscX.grid(row=5, column=2)
        lb_MaxEscX.grid(row=5, column=3)
        ent_MaxEscX.grid(row=5, column=4)
        lb_MinEscY.grid(row=6, column=1)
        ent_MinEscY.grid(row=6, column=2)
        lb_MaxEscY.grid(row=6, column=3)
        ent_MaxEscY.grid(row=6, column=4)
        rb_Transladar.grid(row=7, column=0, sticky=W)
        lb_MinTransX.grid(row=7, column=1)
        ent_MinTransX.grid(row=7, column=2)
        lb_MaxTransX.grid(row=7, column=3)
        ent_MaxTransX.grid(row=7, column=4)
        lb_MinTransY.grid(row=8, column=1)
        ent_MinTransY.grid(row=8, column=2)
        lb_MaxTransY.grid(row=8, column=3)
        ent_MaxTransY.grid(row=8, column=4)
        bt_Salvar.grid()

        ent_MinRot.delete(0, END)
        ent_MaxRot.delete(0, END)
        ent_FlipVert.delete(0, END)
        ent_FlipHoriz.delete(0, END)
        ent_MaxEscX.delete(0, END)
        ent_MaxEscY.delete(0, END)
        ent_MinEscX.delete(0, END)
        ent_MinEscY.delete(0, END)
        ent_MinTransX.delete(0, END)
        ent_MinTransY.delete(0, END)
        ent_MaxTransX.delete(0, END)
        ent_MaxTransY.delete(0, END)

def abrirTransGeo():
    frame_transgeo = FrameTransGeo(root).grid()

class FrameCorteCis(Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.title("DAS - Corte e Cisalhamento")
        lb_Titulo = Label(self,
                          text="Selecione uma opção de transformação geométrica",
                          font='Times 14 bold',
                          anchor=CENTER)
        rb_Cisalhamento =  Radiobutton(self,
                                       text="Cisalhamento",
                                       variable=valor_rb_CorteCis,
                                       value=1)
        lb_MinCis = Label(self, text="Grau mínimo de cisalhamento")
        ent_MinCis = Entry(self, textvariable=valor_ent_MinCis)
        lb_MaxCis = Label(self, text="Grau máximo de cisalhamento")
        ent_MaxCis = Entry(self, textvariable=valor_ent_MaxCis)
        rb_Corte = Radiobutton(self,
                               text="Corte",
                               variable=valor_rb_CorteCis,
                               value=2)
        lb_Corte = Label(self, text="Relação Altura/Largura")
        ent_Corte = Entry(self, textvariable=valor_ent_Corte)
        bt_Salvar = Button(self, text="Salvar", command=salvarCorteCis)

        lb_Titulo.grid(row=0, columnspan=3)
        rb_Cisalhamento.grid(row=1, column=0, sticky=W)
        lb_MinCis.grid(row=1, column=1)
        ent_MinCis.grid(row=1, column=2)
        lb_MaxCis.grid(row=2, column=1)
        ent_MaxCis.grid(row=2, column=2)
        rb_Corte.grid(row=3, column=0, sticky=W)
        lb_Corte.grid(row=3, column=1)
        ent_Corte.grid(row=3, column=2)
        bt_Salvar.grid()

        ent_MinCis.delete(0, END)
        ent_MaxCis.delete(0, END)
        ent_Corte.delete(0, END)

def abrirCorteCis():
    frame_CorteCis = FrameCorteCis(root).grid()

class FrameRuido(Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.title("DAS - Adição de Ruído")
        lb_Titulo = Label(self,
                          text="Selecione se deseja colocar ruído gaussiano nas imagens",
                          font='Times 14 bold',
                          anchor=CENTER)
        cb_RuidoGaus = Checkbutton(self,
                                   text="Ruído Gaussiano",
                                   variable=valor_cb_Ruido
                                   )
        lb_ValorRuido = Label(self, text="Valor do Ruído:")
        ent_ValorRuido = Entry(self, textvariable=valor_ent_ValorRuido)
        lb_DesvioPadrao = Label(self, text='Desvio padrão:')
        ent_DesvioPadrao = Entry(self, textvariable=valor_ent_DesvPad)
        bt_Salvar = Button(self, text="Salvar", command=salvarRuido)

        lb_Titulo.grid(row=0, columnspan=3)
        cb_RuidoGaus.grid(row=1, column=0, sticky=W)
        lb_ValorRuido.grid(row=1, column=1)
        ent_ValorRuido.grid(row=1, column=2)
        lb_DesvioPadrao.grid(row=2, column=1)
        ent_DesvioPadrao.grid(row=2, column=2)
        bt_Salvar.grid()

        ent_ValorRuido.delete(0, END)
        ent_DesvioPadrao.delete(0, END)

def abrirRuido():
    frame_Ruido = FrameRuido(root).grid()


#---------------------------------

#GUI
root = Tk()
root.title("DAS - Data Augmentation System")
root.geometry("600x300+200+100")
root['bg'] = "white"

valor_rb_TransGeo = IntVar()
valor_ent_MinRot = IntVar()
valor_ent_MaxRot = IntVar()
valor_ent_FlipVert = IntVar()
valor_ent_FlipHoriz = IntVar()
valor_ent_MinEscX = IntVar()
valor_ent_MaxEscX = IntVar()
valor_ent_MinEscY = IntVar()
valor_ent_MaxEscY = IntVar()
valor_ent_MinTransX = IntVar()
valor_ent_MaxTransX = IntVar()
valor_ent_MinTransY = IntVar()
valor_ent_MaxTransY = IntVar()

valor_rb_CorteCis = IntVar()
valor_ent_MinCis = IntVar()
valor_ent_MaxCis = IntVar()
valor_ent_Corte = IntVar()

valor_cb_Ruido = IntVar()
valor_ent_ValorRuido = IntVar()
valor_ent_DesvPad = IntVar()


#--------------------------------

#widgets

frame_Home = Frame(root)

bt_TransGeo = Button(frame_Home, text="Transformação Geométrica", background='white', command=abrirTransGeo)
bt_CorteCis = Button(frame_Home, text="Corte/Cisalhamento", background='white', command=abrirCorteCis)
bt_Ruido = Button(frame_Home, text="Adição de Ruído", background='white', command=abrirRuido)
lb_PastaEntrada = Label(frame_Home,
                text="Selecione a pasta do DataSet",
                background='white',
                font='Times 12 bold',
                width=20,
                bd=1,
                height=2,
                anchor=CENTER,
                padx=10,
                pady=5,
                justify=LEFT,
                )
bt_PastaEnt = Button(frame_Home,
                     text="Browse",
                     background='white',
                     bd=1, relief="raised",
                     command=abrirDiretorioEntrada)
lb_PastaSaida = Label(frame_Home,
                text="Selecione a pasta de Saída",
                background='white',
                font='Times 12 bold',
                width=20,
                bd=1,
                height=2,
                anchor=CENTER,
                padx=10,
                pady=5,
                justify=LEFT,
                )
bt_PastaSaida = Button(frame_Home,
                       text="Browse",
                       background='white',
                       bd=1,
                       relief="raised",
                       command=abrirDiretorioSaida)

lb_Qtd = Label(frame_Home,
                text="Quantidade de arquivos a serem gerados a partir de uma imagem",
                background='white',
                font='Times 8 bold',
                width=45,
                bd=1,
                height=5,
                anchor=CENTER,
                padx=10,
                pady=5,
                justify=LEFT,
                )
ent_Qtd=Entry(frame_Home)
bt_Start = Button(frame_Home,
                  text="Start",
                  background='white',
                  bd=1, relief="raised",
                  command=iniciarDataAugmentation)






#-------------------------------------
#Layout
bt_TransGeo.grid(column=0, row=0, sticky=E)
bt_CorteCis.grid(column=1, row=0)
bt_Ruido.grid(column=2, row=0, sticky=W)
lb_PastaEntrada.grid(column=0, row=1)
bt_PastaEnt.grid(column=0, row=2)
lb_PastaSaida.grid(column=2, row=1)
bt_PastaSaida.grid(column=2, row=2)
lb_Qtd.grid(columnspan=2, row=3, column=0)
ent_Qtd.grid(column=2, row=3, sticky=W)
ent_Qtd.focus()
bt_Start.grid(column=1, row=4)
frame_Home['bg'] = "white"

frame_Home.grid()


#--------------------------------------

root.mainloop()
"""
