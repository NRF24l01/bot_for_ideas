create table public.users(
   id INT NOT NULL,
   user_id VARCHAR (20) NOT NULL,
   user_name VARCHAR (20) NOT NULL,
   gen_ideas_count VARCHAR (50),
   warns_count VARCHAR (50),
   rang VARCHAR (50),
   dt_st VARCHAR (50),
   PRIMARY KEY (id)
);
create table public.ideas(
   id INT NOT NULL,
   user_id VARCHAR (20) NOT NULL,
   user_name VARCHAR (20) NOT NULL,
   idea_text VARCHAR (50),
   who_liked VARCHAR (255),
   PRIMARY KEY (id) )
