-- CreateTable
CREATE TABLE "news" (
    "id" SERIAL NOT NULL,
    "title" TEXT NOT NULL,
    "date" DATE NOT NULL,
    "text" TEXT NOT NULL,
    "image" TEXT,

    CONSTRAINT "news_pkey" PRIMARY KEY ("id")
);
