import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { Component, inject, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { environment } from '../environments/environment.generated';

interface CalculateResponse {
  price: number;
  discount_pct: number;
  final_price: number;
  base_cashback: number;
  vip_bonus: number;
  total_cashback: number;
}

interface HistoryItem {
  id: number;
  client_type: string;
  price: number;
  discount_pct: number;
  cashback: number;
  created_at: string;
}

@Component({
  selector: 'app-root',
  imports: [CommonModule, FormsModule],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App implements OnInit {
  private readonly http = inject(HttpClient);
  private readonly apiBaseUrl = environment.apiBaseUrl.replace(/\/$/, '');

  clientType = 'normal';
  price = 600;
  discountPct = 0;
  result: CalculateResponse | null = null;
  history: HistoryItem[] = [];
  loading = false;
  error = '';

  ngOnInit(): void {
    this.loadHistory();
  }

  calculate(): void {
    this.loading = true;
    this.error = '';

    this.http.post<CalculateResponse>(`${this.apiBaseUrl}/calculate`, {
      client_type: this.clientType,
      price: Number(this.price),
      discount_pct: Number(this.discountPct || 0),
    }).subscribe({
      next: (response) => {
        this.result = response;
        this.loading = false;
        this.loadHistory();
      },
      error: (err) => {
        this.error = err?.error?.detail || 'Nao foi possivel calcular o cashback.';
        this.loading = false;
      },
    });
  }

  loadHistory(): void {
    this.http.get<HistoryItem[]>(`${this.apiBaseUrl}/history`).subscribe({
      next: (items) => {
        this.history = items;
      },
      error: () => {
        this.history = [];
      },
    });
  }

  formatCurrency(value: number): string {
    return new Intl.NumberFormat('pt-BR', {
      style: 'currency',
      currency: 'BRL',
    }).format(value);
  }
}
