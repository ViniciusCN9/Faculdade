package controller;

import java.io.IOException;
import java.util.UUID;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import dao.AlunoDao;

public class AlunoController extends HttpServlet {
	private static final long serialVersionUID = 1L;
	
	private static String INDEX = "/index.jsp";
	private static String FORM_ALUNO = "/formAluno.jsp";
	private static String LIST_ALUNO = "/listAluno.jsp";
	private AlunoDao alunoDao;
	
    public AlunoController() {
    	super();
        this.alunoDao = new AlunoDao();
    }

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String forward = "";
        String action = request.getParameter("action");
        
        HttpSession session = request.getSession();
        session.setAttribute("token", UUID.randomUUID().toString());
        
        if (action == null) {
        	forward = INDEX;
        } else if (action.equalsIgnoreCase("list")) {
        	forward = LIST_ALUNO;
        	request.setAttribute("alunos", alunoDao.getAlunos());
        } else if (action.equalsIgnoreCase("insert")) {
        	forward = FORM_ALUNO;
        	request.setAttribute("title", "Adicionar");
        } else if (action.equalsIgnoreCase("update")) {
        	forward = FORM_ALUNO;
        	int id = Integer.parseInt(request.getParameter("id"));
        	request.setAttribute("aluno", alunoDao.getAluno(id));
        	request.setAttribute("title", "Atualizar");
        } else if (action.equalsIgnoreCase("delete")) {
        	forward = LIST_ALUNO;
        	int id = Integer.parseInt(request.getParameter("id"));
        	alunoDao.removeAluno(id);
        	request.setAttribute("alunos", alunoDao.getAlunos());
        } else {
        	forward = INDEX;
        }
		
		RequestDispatcher view = request.getRequestDispatcher(forward);
		view.forward(request, response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String nome = request.getParameter("nome");
		String id = request.getParameter("id");
		
		HttpSession session = request.getSession();
        String tokenSession = (String) session.getAttribute("token");
        String tokenRequest = request.getParameter("token");
		
        if (tokenRequest.equals(tokenSession)) {
    		if (id == null || id.isEmpty()) {
    			alunoDao.insertAluno(nome);
    		} else {
    			alunoDao.updateAluno(Integer.parseInt(id), nome);
    		}
        }
		
		RequestDispatcher view = request.getRequestDispatcher(LIST_ALUNO);
		request.setAttribute("alunos", alunoDao.getAlunos());
        view.forward(request, response);
	}

}
