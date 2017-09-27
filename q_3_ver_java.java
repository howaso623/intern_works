import java.io.*;
public class fractal {
    static int K;
    static int N;
    static char[][] s_i;
    public static void main(String[] args) {

            if(args.length<4){
                returnUsage();
            }
            K = Integer.parseInt(args[0]);
            N = Integer.parseInt(args[1]);
            if(K>3||N>5||K<1||N<1){
                returnUsage();
            }
            s_i = new char[N][N];
            for(int x=0;x<N;x++) {
                char[] argsSplit = args[2 + x].toCharArray();
                for (int y = 0; y < N; y++) {
                    s_i[x][y] = argsSplit[y];
                }
            }

            int nShape = (int) Math.pow((double) N * N, (double) K);

            char[][] result = makeShape(nShape);
            for (int a = 0; a < nShape; a++) {
                for (int b = 0; b < nShape; b++) {
                    System.out.print(result[a][b]);
                }
                System.out.println();
            }

    }
    private static void returnUsage(){
        System.out.println("Usage:java fractal K N s_1 s_2 ... s_N");
        System.out.println("1<=K<=3,1<=N<=5");
        System.out.println("");
        System.out.println("Usage:java fractal K N s_1 s_2 ... s_N");
        System.exit(0);
    }

    private static char[][] makeShape(int n){
        int nParts = n;
        if(nParts<N)return s_i;
        int nextParts = nParts/N;
        char[][] rParts = new char[n][n];
            char[][] Parts = makeShape(nextParts);
            for(int s=0;s<N;s++){
                for(int i=0;i<N;i++){
                    int y = s*nextParts;
                    int x = i*nextParts;
                        for(int s_p =0;s_p<nextParts;s_p++) {
                            for (int i_p = 0; i_p < nextParts; i_p++) {
                                if(s_i[s][i]=='#') {
                                    rParts[s_p +y][i_p + x] = Parts[s_p][i_p];
                                }
                                if(s_i[s][i]=='.') {
                                    rParts[s_p + y][i_p + x] = '.';
                                }
                            }
                        }
                }
            }
        return rParts;
        }
}


