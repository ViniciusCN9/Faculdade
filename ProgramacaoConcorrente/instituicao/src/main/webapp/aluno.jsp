<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="UTF-8"%>
<%@ page import="java.util.List, models.Aluno" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<link rel="stylesheet"
	href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
	integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T"
	crossorigin="anonymous">
<style> 
* {
    border: 0;
    padding: 0;
    margin: 0;
    box-sizing: border-box;
}

html,
body {
    width: 100%;
    height: 100%;
}

body {
    background: #0F2027;
    background: -webkit-linear-gradient(to right, #2C5364, #203A43, #0F2027);
    background: linear-gradient(to right, #2C5364, #203A43, #0F2027);
    display: flex;
    justify-content: center;
    align-items: center;
}

main {
    width: 70%;
    height: 80%;
    background-color: #fffafa;
    padding: 20px;
    box-shadow: rgba(50, 50, 93, 0.25) 0px 30px 60px -12px inset, rgba(0, 0, 0, 0.3) 0px 18px 36px -18px inset;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-evenly;
}

hr {
  margin: 40px 0;
}

.cabecalho {
	flex-grow: 3;
	width: 90%;
	display: flex;
    flex-direction: column;
    justify-content: center;
	align-items: center;
}

.tabela {
	width: 90%;
	flex-grow: 6;
}

.rodape {
	flex-grow: 1;
	display: flex;
    flex-direction: column;
    justify-content: end;
	align-items: center;
}

</style>

<title>Cadastro de alunos</title>
</head>
<body>
<main>
	<div class="cabecalho">
		<h1>Alunos</h1>
		<br>
	</div>
	<div class="tabela">
		<form action="/instituicao/alunos" method="post">
		  <div class="form-row">
		    <div class="col">
		      <input type="text" class="form-control" placeholder="Nome">
		    </div>
			<button type="submit" class="btn btn-primary">Novo</button>
		  </div>
		</form>
		<br>
		<table class="table table-striped table-bordered">
		<thead class="thead-dark">
		<tr>
		<th scope="col">Id</th>
		<th scope="col">Nome</th>
		<th scope="col">Ação</th>
		</thead>
		<tbody>
		<%
		List<Aluno> alunos = (List<Aluno>)request.getAttribute("alunos");
		for (Aluno aluno : alunos) {
		%>
		<tr>
		<th scope="row"><%= aluno.getId()%></th>
		<td><%= aluno.getNome()%></td>
		<td>Ação</td>
		</tr>
		<%
		}
		%>
		</tbody>
		</table>
	</div>
	<div class="rodape">
		<p class="text-secondary">Desenvolvido por Vinicius</p>
	</div>
	
</main>
</body>
</html>