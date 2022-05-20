<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Diagrama de gabarito modelo ENEM</title>

    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <style>
        .bloco-nome {
            display: grid;
            grid-template-columns: repeat(27, 1fr);
        }

        .bloco-nome article {
            height: 45px;
            border: 1px solid #000;
        }
    </style>
</head>

<body>

    <h1 class="text-center">Diagrama de gabarito modelo ENEM</h1>
    <hr>

    <div class="row">
        <div class="col-md-1"></div>
        <div class="col-md-10" id="folha">
            <div class="row pb-4" id="cabecalho">
                <div class="col-md-4">
                    <h1 class="text-left">FOLHA DE<br> RESPOSTA</h1>
                </div>
                <div class="col-md-4">
                    <!-- <h1 class="text-center">Logomarca</h1> -->
                </div>
                <div class="col-md-4">
                    <h1 class="text-right">1º Dia</h1>
                </div>
            </div>

            <div class="row" id="identificacao">
                <div class="col-md-12" style="border: 1px solid #000; border-radius: 10px;">
                    <div class="row">
                        <!-- lado esquerdo do bloco de identificacao -->
                        <div class="col-md-8" style="border-right: 1px solid #000;">
                            <div class="row">
                                <div class="col-md-12">
                                    <h3>Nome completo:</h3>
                                    <div class="bloco-nome">
                                        <?php
                                        for ($i = 0; $i < 54; $i++) {
                                        ?>
                                            <article></article>
                                        <?php
                                        }
                                        ?>
                                    </div>
                                </div>
                                <div class="col-md-6 pt-4 pb-4">
                                    <h6>Unidade: Colégio São José (Unidade mocambinho)</h6>
                                    <h6>[1234] SIMULADO ENEM</h6>
                                    <h6>RA: 123456789</h6>
                                </div>
                                <div class="col-md-6 pt-4 pb-4 text-center">
                                    <h6>Início: 20/05/2022 12:00:00</h6>
                                    <h6>Término: 20/05/2022 17:00:00</h6>
                                </div>
                                <div class="col-md-4">
                                    <h6>Data de nascimento</h6>
                                    <h6>____/____/______</h6>
                                </div>
                                <div class="col-md-8 text-center">
                                    <h6>___________________________________________________</h6>
                                    <h6>Assinatura do participante</h6>
                                </div>
                            </div>
                        </div>

                        <!-- lado direito do blodo de identificacao -->
                        <div class="col-md-4">
                            <div class="row text-center">
                                <div class="col-md-12 bg-primary text-white" style="border-bottom: 1px solid #000; border-radius: 0 10px 0 0;">
                                    <h6>Número de identificação</h6>
                                </div>
                                <div class="col-md-12 pt-1 pb-1" style="border-top: 1px solid #000; border-bottom: 1px solid #000;">
                                    <h6>123456</h6>
                                </div>
                                <div class="col-md-12 bg-primary text-white" style="border-top: 1px solid #000; border-bottom: 1px solid #000;">
                                    <h6>Turma</h6>
                                </div>
                                <div class="col-md-12 pt-1 pb-1" style="border-top: 1px solid #000; border-bottom: 1px solid #000;">
                                    <h6>xxx</h6>
                                </div>
                                <div class="col-md-12" style="border-top: 1px solid #000; border-bottom: 1px solid #000;">
                                    <h6>PARA USO EXCLUSIVO DO CHEFE DE SALA</h6>
                                    <div class="row">
                                        <div class="col-md-8">
                                            <h6>Participante AUSENTE</h6>
                                        </div>
                                        <div class="col-md-4">
                                            <b>Sim ( )</b>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-md-12" style="border-top: 1px solid #000; border-bottom: 1px solid #000;">
                                    <h6 class="text-left">Participante presente deixou o</h6>
                                    <div class="row">
                                        <div class="col-md-8">
                                            <h6 class="text-left">CARTÃO-RESPOSTA em branco</h6>
                                        </div>
                                        <div class="col-md-4">
                                            <b>Sim ( )</b>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-md-12" style="border-top: 1px solid #000;">
                                    <h6>Marque a sua opção de lingua estrangeira</h6>
                                    <div class="row">
                                        <div class="col-md-6"><b>Inglês ( )</b></div>
                                        <div class="col-md-6"><b>Espanhol ( )</b></div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-md-1"></div>
    </div>

</body>

</html>