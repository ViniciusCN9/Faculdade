<%@ page language="java" contentType="text/html; charset=ISO-8859-1" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
		<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
		<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css">
		<link type="text/css" href="style.css" rel="stylesheet" />
		<title>Lista de Alunos</title>
	</head>
	<body>
		<main>
			<h1 class="text-body">Cadastro de alunos</h1>
			<c:choose>
				<c:when test="${alunos.size() == 0 }">
					<div class="list-table" style="border: none">
						<h4 class="mt-3 text-center">Nenhum aluno cadastrado!</h4>
					</div>
				</c:when>
				<c:otherwise>
					<div class="list-table">
						<table class="table table-striped table-borda">
	                        <thead class="thead-dark">
	                            <tr>
	                                <th style="width: 10%">Id</th>
	                                <th style="width: 60%">Nome</th>
	                                <th style="width: 30%" colspan=2>Ação</th>
	                            </tr>
	                        </thead>
	                        <tbody>
	                            <c:forEach items="${alunos}" var="aluno">
	                                <tr>
	                                    <td><c:out value="${aluno.getId()}" /></td>
	                                    <td><c:out value="${aluno.getNome()}" /></td>
	                                    <td><a href="AlunoController?action=update&id=<c:out value="${aluno.getId()}"/>"><i class="bi bi-pencil-square text-warning"></i></a></td>
	                                    <td><a href="AlunoController?action=delete&id=<c:out value="${aluno.getId()}"/>" onclick="return confirm('Deseja remover esse aluno?')"><i class="bi bi-trash3-fill text-danger"></i></a></td>
	                                </tr>
	                            </c:forEach>
	                        </tbody>
	                    </table>
                    </div>
				</c:otherwise>
			</c:choose>
			<a href="AlunoController?action=insert" class="w-25 btn btn-primary font-weight-bold efeito-up" style="text-decoration:none" role="button"><strong>Adicionar</strong></a>
		</main>
	</body>
	<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
	<script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.3/dist/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
</html>