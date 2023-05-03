package controllers;

import java.io.IOException;
import java.util.List;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import connections.DatabaseConnection;
import models.Aluno;

@WebServlet("/alunos")
public class AlunosServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;

	private DatabaseConnection _dbConnection;
	
    public AlunosServlet() {
    	super();
        this._dbConnection = new DatabaseConnection();
    }

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		List<Aluno> alunos = this._dbConnection.getAlunos();
		System.out.println(alunos.size());
		request.setAttribute("alunos", alunos);
		RequestDispatcher rd = request.getRequestDispatcher("/aluno.jsp");
		rd.forward(request, response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String nome = request.getParameter("nome");
		this._dbConnection.insertAluno(nome);
		RequestDispatcher rd = request.getRequestDispatcher("/aluno.jsp");
		rd.forward(request, response);
	}

	protected void doPut(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
	}

	protected void doDelete(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
	}

}
