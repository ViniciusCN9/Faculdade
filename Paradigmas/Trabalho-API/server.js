const express = require('express');
const mysql = require('mysql');
const axios = require('axios');
const crypto = require('crypto');
const { response } = require('express/lib/express');
const app = express();
const port = 3000;

app.set('view engine', 'ejs');
app.use(express.static('public'));

let connection = mysql.createConnection({
    host: 'br452.hostgator.com.br',
    user: 'obreve59_gran',
    password: 'RaEvdlUyfcvG',
    database: 'obreve59_gran'
});

connection.connect(erro => {
    if (erro) {
        console.log('Error connection to database: ' + error.stack);
        return;
    }

    console.log('Connected to database.');
})

app.get('/herois/:page', (req, res) => {
    const page = req.params.page;
    const limit= 20;
    const offset = (page - 1) * limit;

    let query = 'SELECT * FROM herois LIMIT ?, ?';
    let countQuery = 'SELECT COUNT(*) AS total FROM herois';

    connection.query(query, [offset, limit], (error, results) => {
        if (error) {
            res.send('Error executing query: ' + error.stack);
            return;
        }

        connection.query(countQuery, (error, countResults) => {
            if (error) {
                res.send('Error executing count query: ' + error.stack);
                return;
            }

            const totalHerois = countResults[0].total;
            const totalPages = Math.ceil(totalHerois / limit);
            
            res.render('herois', {herois: results, totalPages: totalPages});
        });
    });
});

app.get('/heroi/:id', (req, res) => {
    const heroiId = req.params.id;
    const ts = Date.now();
    const publicKey = '18a4398516432f9bf1c68db7626aa980';
    const privateKey= '66be5b6be8d93e49f5b782cf539b6c907b330a0b';
    const hash = crypto.createHash('md5').update(ts + privateKey + publicKey).digest("hex");

    axios.get(`http://gateway.marvel.com/v1/public/characters/${heroiId}?ts=${ts}&apikey=${publicKey}&hash=${hash}`)
        .then(response => {
            const heroiData = response.data.data.results[0];

            if (!heroiData) {
                return res.status(404).send('Heroinão encontrado.');
            }

            const heroi = {
                id: heroiData.id,
                nome: heroiData.name,
                descricao: heroiData.description,
                imagem: `${heroiData.thumbnail.path}.${heroiData.thumbnail.extension}`,
                hqs: heroiData.comics.items
            };

            res.render('heroi', { heroi: heroi });
        })
        .catch(error => {
            const status = error.response ? error.response.status : 500;
            console.log(`Error status ${status}, message: ${error.message}`);
            res.status(status).send("Erro ao buscar detalhes do heroi." + error);
        });
});

app.get('/encerrar', (req, res) => {
    Server.close(() => {
        console.log('Servidor encerrado.');
        process.exit(0);
    });
});

const server= app.listen(port, () => {
    console.log(`Servidor em execução na porta ${port}`);
});

setInterval(() => {}, 1000);

