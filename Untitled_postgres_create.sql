CREATE TABLE "public.main" (
	"id" serial NOT NULL,
	"brand_model" serial(255) NOT NULL,
	"km" serial NOT NULL,
	"state_of_residence" serial(255) NOT NULL,
	"image" serial NOT NULL,
	"year" serial NOT NULL,
	"price" serial NOT NULL,
	"plate" serial(255) NOT NULL,
	CONSTRAINT "main_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);





