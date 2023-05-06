<%@ page language="java" contentType="text/html; charset=ISO-8859-1" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
		<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
		<link type="text/css" href="style.css" rel="stylesheet" />
		<title>${title} Aluno</title>
	</head>
	<body>
		<main>
			<h1 class="text-body">${title} aluno</h1>
			<form class="form-aluno" method="POST" action='AlunoController' name="form-aluno">
				<input type="hidden" readonly="readonly" name="token" value="<%= session.getAttribute("token")%>" />
                <input type="hidden" readonly="readonly" name="id" value="<c:out value="${aluno.getId()}" />" />
                <div class="d-flex flex-column justify-content-between h-100">
	                <div class="form-group">
	                    <label>Nome</label>
	                    <input type="text" class="form-control" name="nome" value="<c:out value="${aluno.getNome()}" />" />
	                </div>
	                <div class="pt-3 d-flex justify-content-between">
		                <input type="button" onclick="location.href='index.jsp'" class="w-25 btn btn-danger font-weight-bold efeito-up" value="Cancelar">
		                <input type="submit" value="Salvar" class="w-25 btn btn-success font-weight-bold efeito-up" />
	                </div>
                </div>
            </form>
		</main>
	</body>
	<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
	<script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.3/dist/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
</html>