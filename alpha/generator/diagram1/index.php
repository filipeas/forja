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
            height: 35px;
            border: 1px solid #000;
        }

        .marca {
            background-color: #000;
            color: #000;
        }
    </style>
</head>

<body>

    <?php
    require_once 'vendor/autoload.php';
    require_once 'vendor/fzaninotto/Faker/src/autoload.php';
    $faker = Faker\Factory::create();
    ?>

    <h1 class="text-center">Diagrama de gabarito modelo ENEM <br> <button class=" btn btn-success" onclick="generate()">Gerar Folha-Resposta</button></h1>
    <hr>

    <div class="container bg-white p-5" style="padding-right: 150px!important;" id="folha-resposta">
        <?php
        $nomeCompleto = $faker->name . ' ' . $faker->lastname;
        ?>

        <div class="row">
            <div class="col-md-12">
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

                <!-- bloco de identificacao -->
                <div class="row" id="identificacao">
                    <div class="col-md-12" style="border: 1px solid #000; border-radius: 10px;">
                        <div class="row">
                            <!-- lado esquerdo do bloco de identificacao -->
                            <div class="col-md-8" style="border-right: 1px solid #000;">
                                <div class="row">
                                    <div class="col-md-12">
                                        <h5>Nome completo: <?= $nomeCompleto ?></h5>
                                        <div class="bloco-nome">
                                            <?php
                                            for ($i = 0; $i < 54; $i++) {
                                            ?>
                                                <article class="text-center"><?= (isset($nomeCompleto[$i]) ? $nomeCompleto[$i] : '') ?></article>
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
                                        <h6><?= $faker->randomNumber($nbDigits = NULL, $strict = false) ?></h6>
                                    </div>
                                    <div class="col-md-12 bg-primary text-white" style="border-top: 1px solid #000; border-bottom: 1px solid #000;">
                                        <h6>Turma</h6>
                                    </div>
                                    <div class="col-md-12 pt-1 pb-1" style="border-top: 1px solid #000; border-bottom: 1px solid #000;">
                                        <h6><?= $faker->randomNumber($nbDigits = NULL, $strict = false) ?></h6>
                                    </div>
                                    <div class="col-md-12" style="border-top: 1px solid #000; border-bottom: 1px solid #000;">
                                        <h6>PARA USO EXCLUSIVO DO CHEFE DE SALA</h6>
                                        <div class="row">
                                            <div class="col-md-8">
                                                <h6>Participante AUSENTE</h6>
                                            </div>
                                            <div class="col-md-4">
                                                <div class="row">
                                                    <?php
                                                    $marcaParticipanteAusente = rand(0, 1);
                                                    ?>
                                                    <div class="col-md-12 p-1">
                                                        SIM <b class="<?= ($marcaParticipanteAusente === 0 ? 'marca' : '') ?> ml-2" style="border: 1px solid #000; border-radius: 100%; font-size: 9px; padding: 3px 9px 3px 9px;"></b>
                                                    </div>
                                                </div>
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
                                                <div class="row">
                                                    <?php
                                                    $marcaRespostasEmBranco = rand(0, 1);
                                                    ?>
                                                    <div class="col-md-12 p-1">
                                                        SIM <b class="<?= ($marcaRespostasEmBranco === 0 ? 'marca' : '') ?> ml-2" style="border: 1px solid #000; border-radius: 100%; font-size: 9px; padding: 3px 9px 3px 9px;"></b>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-md-12" style="border-top: 1px solid #000;">
                                        <h6>Marque a sua opção de lingua estrangeira</h6>
                                        <?php
                                        $marcaLingua = rand(0, 1);
                                        ?>
                                        <div class="row">
                                            <div class="col-md-6">
                                                <div class="row">
                                                    <div class="col-md-12 p-1">
                                                        Inglês <b class="<?= ($marcaLingua === 0 ? 'marca' : '') ?> ml-2" style="border: 1px solid #000; border-radius: 100%; font-size: 9px; padding: 3px 9px 3px 9px;"></b>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="col-md-6">
                                                <div class="row">
                                                    <div class="col-md-12 p-1">
                                                        Espanhol <b class="<?= ($marcaLingua === 1 ? 'marca' : '') ?> ml-2" style="border: 1px solid #000; border-radius: 100%; font-size: 9px; padding: 3px 9px 3px 9px;"></b>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- bloco de instrucoes -->
                <div class="col-md-12 pt-4 pb-2">
                    <div class="row">
                        <div class="col-md-12 text-center">
                            <h4>INSTRUÇÕES</h4>
                        </div>
                        <div class="col-md-6 text-justify">
                            <ul>
                                <li>Verifique se o seu nome completo, o número da sua inscrição e os demais dados impressos neste <b>CARTÃO-RESPOSTA</b> estão corretos. Preencha o seu nome completo, a data de seu nascimento e assine somente no local apropriado.</li>
                                <li>Transcreva a frase apresentada na CAPA DO SEU <b>CADERNO DE QUESTÕES</b> no local abaixo indicado.</li>
                                <li>Marque neste <b>CARTÃO-RESPOSTA</b> a opção correspondente à <b>COR DA CAPA DO SEU CADERNO DE QUESTÕES</b>.</li>
                                <li><b>O CARTÃO-RESPOSTA</b> é o único documento que será utilizado para a correção eletrônica de suas provas. Não o amasse, não o dobre nem o rasure. O preenchimento do <b>CARTÃO-RESPOSTA</b></li>
                            </ul>
                        </div>
                        <div class="col-md-6">
                            <ul>
                                <li>deve ser feito com caneta esferográfica de <b>tinta preta, fabricada em material transparente</b>. Não será permitido o uso de lápis, lapiseira (grafite) e borracha.</li>
                                <li>Não haverá substituição deste <b>CARTÃO-RESPOSTA</b> por erro de preenchimento do PARTICIPANTE.</li>
                                <li>Faça o preenchimento de suas respostas neste <b>CARTÃO-RESPOSTA</b>, nos campos apropriados, conforme o <b>EXEMPLO DE PREENCHIMENTO</b>.</li>
                                <li>Em nenhuma hipótese você poderá levar este <b>CARTÃO-RESPOSTA</b> ao deixar a sala de provas, sob pena de eliminação do Exame.</li>
                            </ul>
                        </div>
                        <div class="col-md-4 text-justify" style="border: 4px solid #007bff; border-top: 15px solid #007bff; border-bottom: 15px solid #007bff;">
                            <h6><b>ATENÇÃO:</b> TRANSCRVA AQUI COM A SUA CALIGRAFIA USUAL, A FRASE APRESENTADA NA CAPA DO SEU CADERNO DE QUESTÕES. COMFORME AS INSTRUÇÕES NELA CONTIDAS.</h6>
                        </div>
                        <div class="col-md-8" style="border: 1px solid #007bff;"></div>
                        <div class="col-md-12 mt-3 mb-3 text-center" style="border: 2px solid #000;">
                            <h4>MARQUE A OPÇÃO CORRESPONDENTE À COR DA CAPA DO SEU CADERNO DE QUESTÕES</h4>
                            <hr style="background-color: #000;">
                            <?php
                            $corProva = rand(0, 3);
                            ?>
                            <div class="row">
                                <div class="col-md-3 p-1">
                                    <b class="<?= ($corProva === 0 ? 'marca' : '') ?>" style="border: 1px solid #000; border-radius: 100%; font-size: 9px; padding: 3px 7px 3px 7px;">1</b> AZUL
                                </div>
                                <div class="col-md-3 p-1">
                                    <b class="<?= ($corProva === 1 ? 'marca' : '') ?>" style="border: 1px solid #000; border-radius: 100%; font-size: 9px; padding: 3px 7px 3px 7px;">2</b> AMARELO
                                </div>
                                <div class="col-md-3 p-1">
                                    <b class="<?= ($corProva === 2 ? 'marca' : '') ?>" style="border: 1px solid #000; border-radius: 100%; font-size: 9px; padding: 3px 7px 3px 7px;">3</b> BRANCO
                                </div>
                                <div class="col-md-3 p-1">
                                    <b class="<?= ($corProva === 3 ? 'marca' : '') ?>" style="border: 1px solid #000; border-radius: 100%; font-size: 9px; padding: 3px 7px 3px 7px;">4</b> CINZA
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- bloco de questoes -->
                <div class="col-md-12">
                    <div class="row">
                        <?php
                        $numQuestaoAtual = 1;
                        // 6 colunas de questoes
                        for ($j = 0; $j < 6; $j++) {
                        ?>
                            <div class="col-md-2 pl-4 pr-4">
                                <div class="row text-center" style="border: 1px solid #000;">
                                    <div class="col-md-12" style="border-bottom: 1px solid #000;">
                                        <h6 style="font-size: 10px;"><b>QUESTÃO/RESPOSTA</b></h6>
                                    </div>
                                    <?php
                                    for ($i = 0; $i < 15; $i++) {
                                        $marca = rand(0, 4);
                                    ?>
                                        <div class="col-md-12">
                                            <div class="row">
                                                <div class="col-md-2 p-1" style="border-right: 1px solid #000;">
                                                    <h5><b style="font-size: 10px;"><?= ($numQuestaoAtual <= 9 ? '0' . $numQuestaoAtual++ : $numQuestaoAtual++) ?></b></h5>
                                                </div>
                                                <div class="col-md-2 p-1">
                                                    <b class="<?= ($marca === 0 ? 'marca' : '') ?>" style="border: 1px solid #000; border-radius: 100%; font-size: 10px; padding: 2px 5px 2px 5px;">A</b>
                                                </div>
                                                <div class="col-md-2 p-1">
                                                    <b class="<?= ($marca === 1 ? 'marca' : '') ?>" style="border: 1px solid #000; border-radius: 100%; font-size: 10px; padding: 2px 5px 2px 5px;">B</b>
                                                </div>
                                                <div class="col-md-2 p-1">
                                                    <b class="<?= ($marca === 2 ? 'marca' : '') ?>" style="border: 1px solid #000; border-radius: 100%; font-size: 10px; padding: 2px 5px 2px 5px;">C</b>
                                                </div>
                                                <div class="col-md-2 p-1">
                                                    <b class="<?= ($marca === 3 ? 'marca' : '') ?>" style="border: 1px solid #000; border-radius: 100%; font-size: 10px; padding: 2px 5px 2px 5px;">D</b>
                                                </div>
                                                <div class="col-md-2 p-1">
                                                    <b class="<?= ($marca === 4 ? 'marca' : '') ?>" style="border: 1px solid #000; border-radius: 100%; font-size: 10px; padding: 2px 5px 2px 5px;">E</b>
                                                </div>
                                            </div>
                                        </div>
                                    <?php
                                    }
                                    ?>
                                </div>
                            </div>
                        <?php
                        }
                        ?>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script src="node_modules/dom-to-image/dist/dom-to-image.min.js"></script>
    <script>
        console.log('Abrindo página inicial...');

        var folhaResposta = document.getElementById('folha-resposta');

        function generate() {
            domtoimage
                .toBlob(folhaResposta)
                .then(function(blob) {
                    url = window.URL.createObjectURL(blob);
                    var a = document.createElement("a");
                    a.style = "display: none";
                    document.body.appendChild(a);
                    a.href = url;
                    a.download = 'folha.png';
                    a.click();
                    window.URL.revokeObjectURL(url);
                });
        }
    </script>
</body>

</html>